from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def madhav(request):
    return HttpResponse('<h1><b>Jspiders Institute</h1></b>')