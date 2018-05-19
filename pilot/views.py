from django.shortcuts import render
from . import views
# Create your views here.


def landing(request):
    return render(request,'main_templates/landing.html')