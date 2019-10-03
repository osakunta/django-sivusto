from django.forms.fields import CharField, ChoiceField
from django.forms.widgets import Textarea, RadioSelect

from ..forms import ContactsForm


class PalauteForm(ContactsForm):
    msg = CharField(
        label='Mitä haluat sanoa?',
        widget=Textarea
    )

    res = ChoiceField(
        choices=[(True, 'Haluan'), (False, 'En halua')],
        label='Haluatko, että sinulle vastataan?',
        widget=RadioSelect
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
