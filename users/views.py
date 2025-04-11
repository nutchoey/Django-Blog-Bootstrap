from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def RegisterView(request):
    return HttpResponse("Tis is the register users page")
