from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from cohorts.factories import CohortFactory
from cohorts.models import Cohort
from patients.factories import PatientFactory
from patients.models import Patient


class PatientViewsetTestCase(APITestCase):

    def test_retrieve(self):
        c = CohortFactory()
        patients = PatientFactory.create_batch(3)
        c.patients.add(*patients)
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.get(reverse("cohort:cohort-detail", args=(c.pk,)))
        self.assertEqual(response.status_code, 200)

        content = response.json()
        self.assertEqual(content['id'], c.pk)
        self.assertEqual(content['name'], c.name)
        self.assertEqual(content['description'], c.description)
        self.assertEqual(content['created_at'], c.created_at.strftime(settings.REST_FRAMEWORK['DATETIME_FORMAT']))
        self.assertEqual(content['updated_at'], c.updated_at.strftime(settings.REST_FRAMEWORK['DATETIME_FORMAT']))
        self.assertEqual({p['id'] for p in content['patients']}, {p.pk for p in patients})

    def test_list(self):
        c1 = CohortFactory()
        c2 = CohortFactory()
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.get(reverse("cohort:cohort-list"))
        self.assertEqual(response.status_code, 200)

        content = response.json()
        self.assertEqual(content['count'], 2)
        self.assertEqual({c1.pk, c2.pk}, {p['id'] for p in content['results']})

    def test_create(self):
        u = User.objects.create_user("test")
        c = CohortFactory.build(owner=u)
        patients = PatientFactory.create_batch(3)
        payload = {
            "name": c.name,
            "owner": u.pk,
            "description": c.description,
            "patient_ids": (p.pk for p in patients)
        }
        self.assertEqual(Cohort.objects.count(), 0)
        self.client.force_authenticate(u)
        response = self.client.post(reverse("cohort:cohort-list"), data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Cohort.objects.count(), 1)
        self.assertEqual(
            set(Cohort.objects.first().patients.values_list('pk', flat=True)),
            {p.pk for p in patients}
        )

    def test_update(self):
        c = CohortFactory()
        payload = {
            "name": "ANewName",
            "owner": c.owner.pk,
            "description": c.description,
        }
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.put(reverse("cohort:cohort-detail", args=(c.pk,)), data=payload)
        self.assertEqual(response.status_code, 200, response.content)
        c.refresh_from_db()
        self.assertEqual(c.name, "ANewName")

    def test_partial_update(self):
        c = CohortFactory()
        payload = {"name": "ANewName"}
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.patch(reverse("cohort:cohort-detail", args=(c.pk,)), data=payload)
        self.assertEqual(response.status_code, 200)
        c.refresh_from_db()
        self.assertEqual(c.name, "ANewName")

    def test_delete_superuser(self):
        c = CohortFactory()
        self.assertEqual(Cohort.objects.count(), 1)
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.delete(reverse("cohort:cohort-detail", args=(c.pk,)))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Cohort.objects.count(), 0)
