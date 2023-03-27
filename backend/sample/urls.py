from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("api/project", ProjectModelViewSet)
router.register("api/sample-analysis", SampleAnalysisModelViewSet)
router.register("api/product", SampleAnalysisModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls