from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from ..email import EmailService
from .utils import get_palaute_form, construct_message
from . import config


TEMPLATE = 'hallituspalaute.html'
EMAIL_SERVICE = EmailService(config.EMAIL_SUBJECT,
                             config.EMAIL_SENDER,
                             config.EMAIL_RECIPIENTS)


def hallituspalaute(request) -> HttpResponse:
    if request.method in ['GET', 'HEAD']:
        return get_form(request)
    elif request.method == 'POST':
        return submit_form(request)

    return HttpResponseBadRequest('Invalid method')


def get_form(request) -> HttpResponse:
    form = get_palaute_form(user=request.user)
    return render(request, TEMPLATE, dict(form=form))


def submit_form(request) -> HttpResponse:
    form = get_palaute_form(user=request.user, data=request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest('Invalid form data')

    data = form.cleaned_data
    msg = construct_message({name: data[name] for name in form.fields})

    EMAIL_SERVICE.send(msg, data['email'])

    return render(request, TEMPLATE, dict(ok=True))
