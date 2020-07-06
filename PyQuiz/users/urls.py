from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api', UserViewSet, 'users')

urlpatterns = router.urls
