from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .sample.gallery import Gallery


@login_required
def gallery_list(request, gallery_path):
    try:
        gallery = Gallery(gallery_path, '/gallery/')
    except FileNotFoundError:
        raise Http404

    current_path = request.path + '/' if not request.path.endswith('/') else request.path
    context = {'gallery': gallery, 'current_path': current_path}

    return render(request, 'gallery.html', context)
