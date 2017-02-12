from django import forms
from django.shortcuts import render

class PalauteForm(forms.Form):
    msg = forms.CharField(label='Mitä haluat sanoa?', widget=forms.Textarea)
    res = forms.ChoiceField(choices=[(True, 'Haluan'), (False, 'En halua')], label='Haluatko, että sinulle vastataan?', required=True, widget=forms.RadioSelect())
    name = forms.CharField(label="Nimesi")
    email = forms.CharField(label="Sähköpostiosoitteesi")

class PalauteFormLogged(PalauteForm):
    aloite = forms.ChoiceField(choices=[(True, 'Kyllä'), (False, 'Ei')], widget=forms.RadioSelect(), label="Olen osakunnan varsinainen jäsen ja tämä on kirjallinen aloite, jonka haluan hallituksen käsittelevän.", help_text="Osakunnan säännöt §45: Osakunnan varsinaisella jäsenellä on oikeus tekemällään kirjallisella aloitteella saattaa hallituksen toimivaltaan kuuluva asia sen käsiteltäväksi.")

def index(request):
    user = request.user
    if user.is_authenticated():
        form = PalauteFormLogged(initial={ 'email': user.email })
    else:
        form = PalauteForm()

    return render(request, 'hallituspalaute.html', { 'form': form })

