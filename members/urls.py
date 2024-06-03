from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('members/details/<int:pk>', views.details, name='details'),
    path('testing/', views.testing, name='testing')
]