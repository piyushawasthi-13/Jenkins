from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse("ok hello Big brother. kaise ho .....")