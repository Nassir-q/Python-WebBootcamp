from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
]
