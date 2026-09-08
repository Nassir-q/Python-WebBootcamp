from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def upload_view(request):
    context = {}

    if request.method == 'POST' and request.FILES.get('avatar'):
        uploaded_file = request.FILES['avatar']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        context['uploaded_image'] = fs.url(filename)

    return render(request, 'upload.html', context)
