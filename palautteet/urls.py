from django.conf.urls import url

from .hallitus.views import hallituspalaute

urlpatterns = [
    url(r'hallitus', hallituspalaute),
]
