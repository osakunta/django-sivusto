# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from . import views

gallery_images = settings.BASE_DIR + '/gallery-images/'
gallery_thumbs = settings.BASE_DIR + '/media/gallery-thumbs/'
handler404 = views.handler404
handler500 = views.handler500
admin.autodiscover()


@login_required
def protected_image_serve(request, path, document_root=gallery_images, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


@login_required
def protected_thumb_serve(request, path, document_root=gallery_thumbs, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


protected_media = [
    path('gallery-images/(?P<path>.*)$', protected_image_serve),
    path('media/gallery-thumbs/(?P<path>.*)$', protected_thumb_serve),
]

urlpatterns = protected_media + i18n_patterns(
    path('admin/', admin.site.urls),
    path('palautteet/', include('palautteet.urls')),
    path('ilmo/', include('ilmo_app.urls')),
    path('gallery/', include('gallery.urls'), name='gallery'),
    path('', include('auth0login.urls')),
    path('', include('filer.server.urls')),
    path('', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = protected_media + staticfiles_urlpatterns() + urlpatterns
