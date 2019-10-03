from ..email import EmailService
from ..views import get_form_view
from .forms import HairintaForm


TEMPLATE = 'hairintailmoitus.html'
EMAIL_SERVICE = EmailService('Häirintäilmoitus',
                             'hairinta@satakuntatalo.fi',
                             ['kuraattori@satakuntatalo.fi'])


hairintailmoitus = get_form_view(lambda _=None, data=None: HairintaForm(data=data),
                                 TEMPLATE,
                                 EMAIL_SERVICE)
