from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.


def index(request):
    return render(request, 'backend/index.html')


def comment(request, pk):
    return HttpResponse('id: {0}'.format(pk, ))
