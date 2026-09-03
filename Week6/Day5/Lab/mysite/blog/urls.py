from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.list_view, name='list'),
    path('post/<int:post_id>/', views.detail_view, name='detail'),
    path('category/<str:category_name>/', views.category_view, name='category'),
]
