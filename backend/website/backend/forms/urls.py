
from django.urls import path
from . import views

app_name = "mr_sqlite"

urlpatterns = [
    # path('', views.index, name='index'),
    path('form_01_test/', views.form_01_test(), name='form_01_test'),
    # path('my/<slug>/', views.my, name='my_slug'),
]

