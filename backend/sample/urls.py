from rest_framework.routers import SimpleRouter

from .views import ProjectModelViewSet
from .views import SampleAnalysisModelViewSet

router = SimpleRouter()
router.register("api/project", ProjectModelViewSet)
router.register("api/sample-analysis", SampleAnalysisModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls