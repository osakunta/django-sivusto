from django.conf.urls import url

from .hairinta.views import hairintailmoitus
from .hallitus.views import hallituspalaute

urlpatterns = [
    url(r'hallitus', hallituspalaute),
    url(r'hairintailmoitus', hairintailmoitus)
]
