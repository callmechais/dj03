from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def home001(requests):
    return HttpResponseRedirect('static/index.html')