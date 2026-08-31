from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse(
        "<h1>Home</h1> <p>Welcome to Home page</p>"

    )


def aboutpage(request):
    return HttpResponse(
        "<h1>About</h1> <p>Welcome to About page</p>"
    )


def contactpage(request):
    return HttpResponse(
        "<h1>Cotact</h1> <p>Welcome to Contact page</p>"
    )
