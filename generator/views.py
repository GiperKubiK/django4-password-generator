from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    charaters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charaters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('special'):
        charaters.extend(list('!@#$%^&*()-_'))

    if request.GET.get('numbers'):
        charaters.extend(list('0123456789'))

    lenght =  int(request.GET.get('lenght', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(charaters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
