from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def faq(request):
    return render(request, 'pages/faq.html')


def team(request):
    return render(request, 'pages/team.html')
