from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .sample.gallery import Gallery


@login_required
def gallery_list(request, gallery_path):
    gallery = Gallery(gallery_path)
    context = {'gallery': gallery}

    return render(request, 'gallery.html', context)
