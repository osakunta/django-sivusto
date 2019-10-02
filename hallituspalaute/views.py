from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage
# change to django.urls in django 1.10
from django.urls import reverse
from django.conf import settings


class PalauteForm(forms.Form):
    msg = forms.CharField(label='Mitä haluat sanoa?', widget=forms.Textarea)
    res = forms.ChoiceField(choices=[(True, 'Haluan'), (False, 'En halua')], label='Haluatko, että sinulle vastataan?', required=True, widget=forms.RadioSelect())
    name = forms.CharField(label="Nimesi", required=False)
    email = forms.EmailField(label="Sähköpostiosoitteesi", required=False)


class PalauteFormLogged(PalauteForm):
    aloite = forms.ChoiceField(
        choices=[(True, 'Kyllä'), (False, 'Ei')],
        widget=forms.RadioSelect(),
        label="Olen osakunnan varsinainen jäsen ja tämä on kirjallinen aloite, jonka haluan hallituksen käsittelevän.",
        help_text="Osakunnan säännöt §45: Osakunnan varsinaisella jäsenellä on oikeus tekemällään kirjallisella aloitteella saattaa hallituksen toimivaltaan kuuluva asia sen käsiteltäväksi."
    )


def thanks(request):
    return render(request, 'kiitos.html')


def index(request):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            form = PalauteFormLogged(request.POST, initial={ 'email': user.email })
        else:
            form = PalauteForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if data['email'] != '':
                sender = data['email']
            else:
                sender = 'noreply@satakuntalainenosakunta.fi'

            msg = ""
            for key in ['msg', 'res', 'name', 'email']:
                msg += form.fields[key].label + ':\n'
                msg += data[key] + '\n\n'

            email = EmailMessage(
                'Postia SatO:n hallitukselle',
                msg,
                settings.HALLITUSPALAUTE_SENDER,
                settings.HALLITUSPALAUTE_RECIPIENTS,
                [],
                reply_to=[sender],
            )
            email.send()

            return HttpResponseRedirect(reverse(thanks))
    else:
        if user.is_authenticated:
            form = PalauteFormLogged(initial={ 'email': user.email })
        else:
            form = PalauteForm()

    return render(request, 'hallituspalaute.html', { 'form': form })
