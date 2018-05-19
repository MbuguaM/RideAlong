from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print(dir(request))
    print(request.body)
    return HttpResponse('<h1>this is a trial</h1>')