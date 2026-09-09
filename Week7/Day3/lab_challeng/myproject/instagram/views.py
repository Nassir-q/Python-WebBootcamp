from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def feed_view(request):
    error_msg = None

    if request.method == 'POST':
        username = request.POST.get('username')
        description = request.POST.get('description')

        image = request.FILES.get('image')

        if image:

            ext = image.name.split('.')[-1].lower()
            if ext in ['jpg', 'jpeg', 'png']:

                Post.objects.create(username=username,
                                    description=description, image=image)
                return redirect('feed')
            else:

                error_msg = "Invalid file type! Only JPG, JPEG, and PNG are allowed."

    posts = Post.objects.all().order_by('-id')
    return render(request, 'upload.html', {'posts': posts, 'error_msg': error_msg})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('feed')
