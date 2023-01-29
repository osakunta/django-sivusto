from django.forms.fields import CharField, BooleanField
from django.forms.widgets import Textarea, CheckboxInput, TextInput

from captcha.fields import ReCaptchaField

from ..forms import ContactsForm


class HairintaForm(ContactsForm):

    class Media:
        js = ('js/conditional_fields.js',)

    msg = CharField(
        label='Kerro omin sanoin tapahtuneesta.',
        widget=Textarea
    )

    msg1 = CharField(
        label='Oliko paikalla muita henkilöitä?',
        widget=Textarea
    )

    res = BooleanField(
        label='Haluan, että minulle vastataan.',
        widget=CheckboxInput(attrs=dict(onclick='contactMe("res", ["name", "email"])')),
        required=False
    )

    captcha = ReCaptchaField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('email').widget = TextInput(attrs=dict(style='display: none'))
        self.fields.get('name').widget = TextInput(attrs=dict(style='display: none'))


