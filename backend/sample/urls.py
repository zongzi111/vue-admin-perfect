from rest_framework.routers import SimpleRouter

from .views import ProjectModelViewSet

router = SimpleRouter()
router.register("api/project", ProjectModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls