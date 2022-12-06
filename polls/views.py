from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime

# Create your views here.
def index(request):

    return HttpResponse("Hello, world!, Check out our first django app")
