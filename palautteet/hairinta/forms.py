from django.forms import Form
from django.forms.fields import CharField, EmailField, BooleanField
from django.forms.widgets import Textarea, CheckboxInput, HiddenInput, TextInput


class HairintaForm(Form):

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
        widget=CheckboxInput(attrs=dict(onclick='contact_me("res", ["name", "email"])'))
    )

    name = CharField(
        label="Nimesi",
        required=False,
        widget=TextInput(attrs=dict(style='display: none'))
    )

    email = EmailField(
        label="Sähköpostiosoitteesi",
        required=False,
        widget=TextInput(attrs=dict(style='display: none'))
    )
