from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from ..email import EmailService, construct_message
from .forms import HairintaForm
from . import config


TEMPLATE = 'hairintailmoitus.html'
EMAIL_SERVICE = EmailService(config.EMAIL_SUBJECT,
                             config.EMAIL_SENDER,
                             config.EMAIL_RECIPIENTS)


def hairintailmoitus(request) -> HttpResponse:
    if request.method in ['GET', 'HEAD']:
        return get_form(request)
    elif request.method == 'POST':
        return submit_form(request)

    return HttpResponseBadRequest('Invalid method')


def get_form(request) -> HttpResponse:
    return render(request, TEMPLATE, dict(form=HairintaForm()))


def submit_form(request) -> HttpResponse:
    form = HairintaForm(data=request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest('Invalid form data')

    data = form.cleaned_data
    msg = construct_message({name: data[name] for name in form.fields})

    EMAIL_SERVICE.send(msg, data['email'])

    return render(request, TEMPLATE, dict(ok=True))
