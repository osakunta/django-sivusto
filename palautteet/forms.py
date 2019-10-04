from collections import OrderedDict

from django.forms import Form
from django.forms.fields import EmailField, CharField


class ContactsForm(Form):
    name = CharField(
        label="Nimesi",
        required=False
    )

    email = EmailField(
        label="Sähköpostiosoitteesi",
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = list(self.fields.keys())[2:] + ['name', 'email']
        self.fields = OrderedDict((k, self.fields[k]) for k in fields)
