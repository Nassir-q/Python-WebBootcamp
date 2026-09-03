from django.shortcuts import render

# Create your views here.


def list_view(request):
    return render(request, 'list.html')


def detail_view(request, post_id):
    return render(request, 'detail.html', {'post_id': post_id})


def category_view(request, category_name):
    return render(request, 'category.html', {'category_name': category_name})
