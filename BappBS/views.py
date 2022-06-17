from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("Hellow world from home page/ index page of Bootstrap practice")
    return render(request, 'base.html')


def home(request):
    paralalxImg = "media/bgs/claudio-testa-U3F2o6vz3bs-unsplash.jpg"
    # return HttpResponse("Hellow world from home page/ index page of Bootstrap practice")
    return render(request, 'home.html', {'paralalxImgHTML': paralalxImg})


0
