from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_home(request):
    return HttpResponse("Heej, du är bäst!")