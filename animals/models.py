from django.db import models
from users.models import Client, User
from django.urls import reverse
from PIL import Image


class Animal(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    )
    gender = models.CharField(max_length=12, choices=GENDER, default='U')
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    notes = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['age']

    def get_absolute_url(self):
        return reverse('animal-detail', kwargs={'pk': self.pk})


class Stray(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    )
    gender = models.CharField(max_length=12, choices=GENDER, default='U')
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    notes = models.CharField(max_length=300)
    arrival_date = models.DateTimeField()
    image = models.ImageField(default='stray.jpg', upload_to='stray_pics')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['arrival_date']


    def get_absolute_url(self):
        return reverse('animal-adoptions')