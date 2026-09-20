from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set-theme/<str:chosen_theme>/', views.set_theme, name='set_theme'),
    path('add-to-cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]
