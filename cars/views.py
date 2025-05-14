from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Avto
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView

def home_page(request):
    cars = Avto.objects.all()  # or whatever logic you need
    return render(request, 'home.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Avto, id=car_id)
    return render(request, 'car_detail.html', {'car': car})


def all_cars(request):
    cars = Avto.objects.all()
    return render(request, 'all_cars.html', {'cars': cars})