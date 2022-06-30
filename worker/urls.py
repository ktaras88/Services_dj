from django.urls import path

from . import views

app_name = 'worker'
urlpatterns = [
    path('', views.appointment, name='appointment'),
]