from django.shortcuts import render
from .models import CarCategory
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.


def index(request):
    return render(request, 'backend/index.html')


def cars(request):
    categories = CarCategory.objects.all()
    return render(request, 'backend/cars.html', {'categories': categories})
