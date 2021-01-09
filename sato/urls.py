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

handler404 = views.handler404
handler500 = views.handler500
admin.autodiscover()

# Use Auth0 login in admin panel.
admin.site.login = login_required(admin.site.login)


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path('palautteet/', include('palautteet.urls')),
    path('ilmo/', include('ilmo_app.urls')),
    path('', include('auth0login.urls')),
    path('', include('filer.server.urls')),
    path('', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = staticfiles_urlpatterns() + urlpatterns
