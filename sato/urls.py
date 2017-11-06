# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from . import views
import sato.settings

@login_required
def protected_serve(request, path, document_root=settings.MEDIA_ROOT + '/gallery-images/', show_indexes=False):
    return serve(request, path, document_root, show_indexes)

admin.autodiscover()

protected_media = [
    url(r'^media/gallery-images/(?P<path>.*)$', protected_serve),
    url(r'^media/media/gallery-images/(?P<path>.*)$', protected_serve),
]

urlpatterns = protected_media + i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'} , name='login'),
    url(r'^logout/$', views.logout_user),
    url(r'^hallituspalaute/', include('hallituspalaute.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^', include('registration.backends.hmac.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('filer.server.urls')),
    url(r'^', include('cms.urls')),
)

# If we have ilmo, add it
if "ilmo_app" in sato.settings.INSTALLED_APPS:
    urlpatterns = i18n_patterns('',
        url(r'^ilmo/', include('ilmo_app.ilmo_app.urls')),
    ) + urlpatterns

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = protected_media + [
         url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ] + staticfiles_urlpatterns() + urlpatterns  # NOQA
