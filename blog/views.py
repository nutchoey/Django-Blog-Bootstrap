from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bloglist(request):
    return HttpResponse("Tis is the blog list page")