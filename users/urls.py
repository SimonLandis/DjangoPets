from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.client_home, name="employee_home.html")
]