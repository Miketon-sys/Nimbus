from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-world/', views.my_worlds, name='my_worlds'),
]