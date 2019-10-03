from .utils import get_palaute_form
from ..email import EmailService
from ..views import get_form_view

TEMPLATE = 'hallituspalaute.html'
EMAIL_SERVICE = EmailService('Postia SatO:n hallitukselle',
                             'hallituspalaute@satakuntatalo.fi',
                             ['hallitus@satakuntatalo.fi'])


hallituspalaute = get_form_view(get_palaute_form,
                                TEMPLATE,
                                EMAIL_SERVICE)
