from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def about_viwe(request):
    return render(request, 'about.html')


def contact_viwe(request):
    return render(request, 'contact.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
