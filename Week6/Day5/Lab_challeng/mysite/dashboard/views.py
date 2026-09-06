from django.shortcuts import render
from django.views import View

# Create your views here.


def home_view(request):
    return render(request, 'home.html')


class ReportsView(View):
    def get(self, request):
        return render(request, 'reports.html')
