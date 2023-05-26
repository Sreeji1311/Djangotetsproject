from django.shortcuts import render
from django.http import HttpResponse
from .models import  Product

# Create your views here.


def index(request):
    return HttpResponse("Hi Dears")


def test_fun(request):
    return render(request, 'test.html')


def course_fun(request):
    return render(request, 'course.html')
