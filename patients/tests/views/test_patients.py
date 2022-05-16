from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from patients.factories import PatientFactory
from patients.models import Patient


class PatientViewsetTestCase(APITestCase):

    def test_retrieve(self):
        p = PatientFactory()
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.get(reverse("patient:patient-detail", args=(p.pk,)))
        self.assertEqual(response.status_code, 200)

        content = response.json()
        self.assertEqual(content['id'], p.pk)
        self.assertEqual(content['first_name'], p.first_name)
        self.assertEqual(content['last_name'], p.last_name)
        self.assertEqual(content['birth_date'], p.birth_date.strftime("%Y-%m-%d"))
        self.assertEqual(content['sex'], p.sex)
        self.assertEqual(content['residence_country'], p.residence_country)

    def test_list(self):
        p1 = PatientFactory()
        p2 = PatientFactory()
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.get(reverse("patient:patient-list"))
        self.assertEqual(response.status_code, 200)

        content = response.json()
        self.assertEqual(content['count'], 2)
        self.assertEqual({p1.pk, p2.pk}, {p['id'] for p in content['results']})

    def test_create(self):
        payload = {
            "first_name": "Jean",
            "last_name": "Dupont",
            "birth_date": (timezone.now() - timedelta(days=365 * 20)).strftime("%Y-%m-%d"),
            "sex": "M",
            "residence_country": "France",
        }
        self.assertEqual(Patient.objects.count(), 0)
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.post(reverse("patient:patient-list"), data=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Patient.objects.count(), 1)

    def test_update(self):
        p = PatientFactory()
        new_country = "Belgium" if p.residence_country != "Belgium" else "France"
        payload = {
            "first_name": p.first_name,
            "last_name": p.last_name,
            "birth_date": p.birth_date.strftime("%Y-%m-%d"),
            "sex": p.sex,
            "residence_country": new_country,
        }
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.put(reverse("patient:patient-detail", args=(p.pk,)), data=payload)
        self.assertEqual(response.status_code, 200)
        p.refresh_from_db()
        self.assertEqual(p.residence_country, new_country)

    def test_partial_update(self):
        p = PatientFactory()
        payload = {"residence_country": "Belgium" if p.residence_country != "Belgium" else "Frances"}
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.patch(reverse("patient:patient-detail", args=(p.pk,)), data=payload)
        self.assertEqual(response.status_code, 200)
        p.refresh_from_db()
        self.assertEqual(p.residence_country, "Belgium")

    def test_delete_superuser(self):
        p = PatientFactory()
        self.assertEqual(Patient.objects.count(), 1)
        self.client.force_authenticate(User.objects.create_user("test"))
        response = self.client.delete(reverse("patient:patient-detail", args=(p.pk,)))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Patient.objects.count(), 0)

