from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.years),
    url(r'^(?P<year>[0-9]{4})/$', views.gallery_list),
    url(r'^(?P<year>[0-9]{4})/(?P<gallery>.*)/$', views.gallery),
]
