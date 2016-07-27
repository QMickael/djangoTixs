from django.conf.urls import url
from django.views.generic import ListView
from backend.models import Locality
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^agencies', ListView.as_view(model=Locality, context_object_name='localities', template_name='backend/agency.html')),
    url(r'^cars', views.cars, name='cars'),
]