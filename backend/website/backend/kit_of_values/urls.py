from rest_framework import routers
from sample_values_v2.views import KitViewSet
router = routers.DefaultRouter()
urlpatterns = [
]

router.register('kit', KitViewSet)


urlpatterns += router.urls

