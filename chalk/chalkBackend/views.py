from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world.")


def hi(request):
    return HttpResponse("HI 3p")