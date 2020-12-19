from django import forms
from .models import Animal, Stray


class RegisterPet(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'age', 'gender', 'species', 'breed', 'notes', 'owner']


class RegisterStray(forms.ModelForm):
    class Meta:
        model = Stray
        fields = ['name', 'age', 'gender', 'species', 'breed', 'notes', 'arrival_date', 'image']