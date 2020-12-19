from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from .models import Animal, Stray


def animal_home(request):
    return render(request, 'animal_home.html')


def about(request):
    return render(request, 'about.html')


class AnimalListView(ListView):
    model = Animal
    template_name = "all_animals.html"
    context_object_name = "animals"
    paginate_by = 5


class AnimalCreateView(CreateView):
    model = Animal
    fields = ['name', 'age', 'gender', 'species', 'breed', 'notes', 'owner']


class AnimalDetailView(DetailView):
    model = Animal


class StrayListView(ListView):
    model = Stray
    template_name = "available_animals.html"
    context_object_name = "strays"
    paginate_by = 5


class StrayCreateView(CreateView):
    model = Stray
    fields = ['name', 'age', 'gender', 'species', 'breed', 'notes', 'arrival_date', 'image']


class StrayDetailView(DetailView):
    model = Stray
