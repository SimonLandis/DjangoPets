from django.shortcuts import render
from .models import Employee
from django.views.generic import (
    CreateView,
    UpdateView
)


def employee_home(request):
    return render(request, 'employee_home.html')


class EmployeeCreateView(CreateView):
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number']

