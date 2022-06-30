from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('', views.MenuView.as_view(), name='menu'),
    path('workers/', views.WorkersView.as_view(), name='workers'),
    path('workers/<int:pk>/', views.ServiceView.as_view(), name='services'),
    path('workers/<int:pk>/date_time/', views.date_time, name='date_time'),
]