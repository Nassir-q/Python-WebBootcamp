from django.urls import path
from . import views
app_name = "students"
urlpatterns = [

    path('', views.home, name='home'),


    path('courses/', views.course_list, name='courses'),


    path('courses/<int:course_id>/', views.course_detail, name='courses_detail'),
]
