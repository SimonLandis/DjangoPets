from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from animals import views as animals_views
from employees import views as employee_views
from users import views as users_views
from animals.views import AnimalListView, AnimalCreateView, StrayCreateView, StrayListView, AnimalDetailView, StrayDetailView
from employees.views import EmployeeCreateView
from django.conf import settings
from django.conf.urls.static import static
from users.views import PetListView, PetCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', animals_views.animal_home, name="animal-home"),
    path('animals/new', AnimalCreateView.as_view(template_name="animal_form.html"), name="animal-create"),
    path('animal/<int:pk>', AnimalDetailView.as_view(template_name="animal_detail.html"), name="animal-detail"),
    path('adoptions/', StrayListView.as_view(), name="animal-adoptions"),
    path('adoptions/new', StrayCreateView.as_view(template_name="stray_form.html"), name="stray-create"),
    path('adoptions/<int:pk>', StrayDetailView.as_view(template_name="available_animal_detail.html"), name="stray-detail"),
    path('clients/', users_views.client_home, name="client-home"),
    path('clients/home', PetListView.as_view(template_name="client_pets.html"), name="client-pets"),
    path('clients/register', users_views.register, name="register"),
    path('clients/login', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('clients/logout', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('clients/profile', users_views.profile, name='profile'),
    path('clients/pets/new', PetCreateView.as_view(template_name="animal_form.html"), name='pet-new'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
