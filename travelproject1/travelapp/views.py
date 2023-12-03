from django.shortcuts import render
from . models import  Place
from .models import tips

# Create your views here.
from django.http import HttpResponse


def demo(request):
    obj=Place.objects.all()
    obj1=tips.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
