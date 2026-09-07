from django.shortcuts import render


def home_view(request):

    context = {'title': 'Home Page', 'is_active': True}
    return render(request, 'home/home.html', context)


def about_view(request):
    context = {'title': 'About'}
    return render(request, 'home/about.html', context)


def services_view(request):

    context = {
        'title': 'Our Services',
        'services': ['Web Development', 'UI/UX Design', 'Database Management'],
    }
    return render(request, 'home/services.html', context)
