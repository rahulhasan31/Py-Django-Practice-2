from django.shortcuts import render

# Create your views here.


def home(requ):
    return render(requ, "home.html" )
 