from django.forms import Form
from django.forms.fields import CharField, ChoiceField, EmailField
from django.forms.widgets import Textarea, RadioSelect


class PalauteForm(Form):
    msg = CharField(
        label='Mitä haluat sanoa?',
        widget=Textarea
    )

    res = ChoiceField(
        choices=[(True, 'Haluan'), (False, 'En halua')],
        label='Haluatko, että sinulle vastataan?',
        widget=RadioSelect
    )

    name = CharField(
        label="Nimesi",
        required=False
    )

    email = EmailField(
        label="Sähköpostiosoitteesi",
        required=False
    )


class PalauteFormLogged(PalauteForm):
    aloite = ChoiceField(
        choices=[(True, 'Kyllä'), (False, 'Ei')],
        widget=RadioSelect,
        label=("Olen osakunnan varsinainen jäsen ja tämä on kirjallinen "
               "aloite, jonka haluan hallituksen käsittelevän."),
        help_text=("Osakunnan säännöt §45: Osakunnan varsinaisella jäsenellä "
                   "on oikeus tekemällään kirjallisella aloitteella saattaa "
                   "hallituksen toimivaltaan kuuluva asia sen käsiteltäväksi.")
    )
