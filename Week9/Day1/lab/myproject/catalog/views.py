from django.http import HttpResponse


def index(request):
    return HttpResponse("catalog is wired up.")
