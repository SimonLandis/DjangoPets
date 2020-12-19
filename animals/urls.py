from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.animal_home, name="animal_home.html")
]