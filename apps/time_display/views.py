from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, strftime
from datetime import datetime

def index(request):
    context = {
    "name": "bob",
    "date": strftime("%b %d, %Y", gmtime()),
    "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)