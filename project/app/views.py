from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HTTPResponse("ok hello brother..")