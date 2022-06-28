from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.

def form_01_test(request: HttpRequest, slug=None):
    return HttpResponse(f"  <h1>  pcs </h1> :  '{slug}' ")
