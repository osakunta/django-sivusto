import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.views.decorators.cache import cache_page

path="media/gallery-images"

for_a_day = 60**2 * 24

@cache_page(for_a_day)
@login_required
def years(request):
    year_list = os.listdir(path)
    year_list.sort(reverse = True)
    return render(request, 'years.html', {'years': year_list})

@cache_page(for_a_day)
@login_required
def gallery_list(request, year=2017):
    galleries_path = path + '/' + year
    galleries = os.listdir(galleries_path)
    galleries.sort(reverse = True, key = lambda x: os.path.getmtime(galleries_path + '/' + x))
    return render(request, 'galleries.html', {'galleries': galleries, 'year': year})

@cache_page(for_a_day)
@login_required
def gallery(request, year, gallery):
    images = os.listdir(path + '/' + year + '/' + gallery)
    images.sort()
    gallery_path = '/' + path + '/' + year + '/' + gallery + '/'
    return render(request, 'gallery.html', {'images': images, 'year': year, 'gallery': gallery, 'path': gallery_path})
