from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cohorts.models import Cohort
from cohorts.serializers import CohortSerializer
from commons.permissions import ReadOnly, IsAuthenticated


class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ReadOnly | IsAuthenticated]
