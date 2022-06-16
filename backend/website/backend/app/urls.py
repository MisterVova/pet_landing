from garpixcms.urls import urlpatterns  # noqa
from django.urls import path, include

# urlpatterns = [] + urlpatterns  # noqa
urlpatterns = [
                  # path('drf-auth/', include('rest_framework.urls')),
                  # path('auth/', include('djoser.urls')),
                  # path('auth/', include('djoser.urls.authtoken')),

                  # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                  # path('api/v0/service/', include('photo_albums.api.v0.urls')),
                  # path('api/v0/user/', include('user.api.v0.urls')),
                  path('api/v1/', include('sample_values_v2.urls')),

                  # path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),

              ] +  urlpatterns  # noqa
