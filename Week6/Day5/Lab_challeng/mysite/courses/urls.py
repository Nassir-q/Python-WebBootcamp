from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('list/', views.list_view, name='list'),
    path('detail/<slug:slug>/', views.course_detail, name='detail'),
    path('category/<str:category_name>/', views.category_view, name='category'),
]
