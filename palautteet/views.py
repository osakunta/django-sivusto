from typing import Callable, Optional

from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
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


def get_form_view(
    form_fn: Callable[[User,  Optional[dict]], ContactsForm],
    template_name: str,
    service: AbstractEmailService
) -> Callable[[HttpRequest], HttpResponse]:
    """

    :param form_fn: a callable that has User (and optionally form data) as parameters
                    producing a Form as a result
    :param template_name: name of the template to be rendered
    :param service: EmailService which is used to send out the form submission
    :return: callable (HttpRequest) -> HttpResponse
    """

    def fn(request):
        if request.method in ['GET', 'HEAD']:
            form = form_fn(request.user, None)
            return get_form(request, form, template_name)
        elif request.method == 'POST':
            form = form_fn(request.user, request.POST)
            return submit_form(request, form, template_name, service)
        return HttpResponseBadRequest('Invalid method')
    return fn
