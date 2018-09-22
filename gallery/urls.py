from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<gallery_path>.*)$', views.gallery_list),
]
