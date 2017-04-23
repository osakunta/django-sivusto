import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.static import serve

path="media/gallery-images"

@login_required
def years(request):
    year_list = os.listdir(path)
    year_list.sort(reverse=True)
    return render(request, 'years.html', {'years': year_list})

@login_required
def gallery_list(request, year=2017):
    galleries = os.listdir(path + '/' + year)
    return render(request, 'galleries.html', {'galleries': galleries, 'year': year})

@login_required
def gallery(request, year, gallery):
    images = os.listdir(path + '/' + year + '/' + gallery)
    gallery_path = '/' + path + '/' + year + '/' + gallery + '/'
    return render(request, 'gallery.html', {'images': images, 'year': year, 'gallery': gallery, 'path': gallery_path})
