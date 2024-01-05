from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v2'

router = DefaultRouter()
router.register('task', TaskModelViewSet, basename='task')

urlpatterns = router.urls