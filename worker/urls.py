from django.urls import path

from . import views

app_name = 'worker'
urlpatterns = [
    path('', views.date_time, name='date_time'),
]