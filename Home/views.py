from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def signUp(request):
    return render(request, 'SignUp.html')



