from django.shortcuts import render

# Create your views here.


def list_view(request):
    return render(request, 'list.html')


def course_detail(request, slug):
    return render(request, 'detail.html', {'slug': slug})


def category_view(request, category_name):
    return render(request, 'category.html', {"category_name": category_name})
