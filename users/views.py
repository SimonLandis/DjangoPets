from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from animals.models import Animal
from users.models import Profile
from django.http import JsonResponse


def client_home(request):
    pets = Animal.objects.filter(owner=request.user)
    context = {
        'pets': pets,
    }
    return render(request, 'client_home.html', context)


class PetListView(ListView):
    model = Animal
    context_object_name = 'pets'
    ordering = ['age']


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


class PetCreateView(CreateView):
    model = Animal
    fields = ['name', 'age', 'species', 'gender']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

