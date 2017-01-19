from django.shortcuts import render
from django.shortcuts import  HttpResponse
# Create your views here.
def index(request):
    #request.post
    #request.get
    return HttpResponse("hello world")
