from rest_framework.routers import DefaultRouter

from . import views

app_name = "cohorts"

router = DefaultRouter()
router.register(r'cohorts', views.CohortViewSet, basename='cohort')

urlpatterns = router.urls
