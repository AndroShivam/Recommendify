from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home')
]
