from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .sample.gallery import Gallery


@login_required
def gallery_list(request, gallery_path):
    gallery = Gallery(gallery_path)
    current_path = request.path + '/' if not request.path.endswith('/') else request.path
    context = {'gallery': gallery, 'current_path': current_path}

    return render(request, 'gallery.html', context)
