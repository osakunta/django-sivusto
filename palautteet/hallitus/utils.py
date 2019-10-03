from .forms import PalauteForm, PalauteFormLogged
from django.contrib.auth.models import User


def get_palaute_form(user: User, data: dict = None) -> PalauteForm:
    if user.is_authenticated:
        return PalauteFormLogged(data, initial=dict(email=user.email))
    else:
        return PalauteForm(data)
