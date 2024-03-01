from django.http import HttpResponse
from django.shortcuts import render

# Görünüm (view) dosyanız
def index(request):
    return HttpResponse("<h1> istün </h1>")
