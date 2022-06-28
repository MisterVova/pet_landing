from garpixcms.urls import *  # noqa

urlpatterns = [

path('forms/', include('forms.urls')),
              ] + urlpatterns  # noqa
