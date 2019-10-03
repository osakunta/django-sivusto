from typing import Callable, Union

from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

from .forms import ContactsForm
from .email import AbstractEmailService


def _send_email(form: ContactsForm, service: AbstractEmailService):
    data = form.cleaned_data
    fields = {name: data[name] for name in form.fields}
    email = data['email']

    service.send(fields, email)


def get_form(request, form: ContactsForm, template_name: str) -> HttpResponse:
    return render(request, template_name, dict(form=form))


def submit_form(request, form: ContactsForm, template_name: str, service: AbstractEmailService) -> HttpResponse:
    if not form.is_valid():
        return HttpResponseBadRequest('Invalid form data')
    _send_email(form, service)
    return render(request, template_name, dict(ok=True))


def get_form_view(form_fn: Union[Callable[[User], ContactsForm],
                                 Callable[[User,  dict], ContactsForm]],
                  template_name: str,
                  service: AbstractEmailService):
    def fn(request):
        if request.method in ['GET', 'HEAD']:
            form = form_fn(request.user)
            return get_form(request, form, template_name)
        elif request.method == 'POST':
            form = form_fn(request.user, request.POST)
            return submit_form(request, form, template_name, service)
        return HttpResponseBadRequest('Invalid method')
    return fn
