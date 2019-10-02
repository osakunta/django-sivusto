from typing import Mapping

from .forms import PalauteForm, PalauteFormLogged
from django.contrib.auth.models import User


def get_palaute_form(*, user: User, data=None) -> PalauteForm:
    if user.is_authenticated:
        return PalauteFormLogged(data, initial=dict(user.email))
    else:
        return PalauteForm(data)


def construct_message(data: Mapping[str, str]) -> str:
    return '\n\n'.join(f'{k}:\n{v}' for k, v in data.items())
