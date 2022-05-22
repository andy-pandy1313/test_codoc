from rest_framework.routers import DefaultRouter

from . import views

app_name = "cohorts"

router = DefaultRouter()
router.register(r'cohorts', views.CohortViewSet, basename='cohort')
router.register(r'comment', views.CommentsViewSet, basename='comment')

urlpatterns = router.urls
