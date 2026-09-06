from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('receipt/<int:receipt_id>/', views.receipt_view, name='receipt')
]
