from unittest.mock import MagicMock
from django.test import TestCase

from palautteet.hallitus.utils import get_palaute_form
from palautteet.hallitus.forms import PalauteForm, PalauteFormLogged


class TestUtils(TestCase):
    def test_right_form_returned_by_user_authentication(self):
        user = MagicMock()

        user.is_authenticated = False
        res = get_palaute_form(user=user)
        self.assertIsInstance(res, PalauteForm)

        user.is_authenticated = True
        res = get_palaute_form(user=user)
        self.assertIsInstance(res, PalauteFormLogged)

    def test_initial_set(self):
        field, value = 'email', 'foo@bar.fi'

        user = MagicMock()
        user.is_authenticated = True
        user.email = {field: value}

        res = get_palaute_form(user=user)
        self.assertDictEqual({field: value}, res[field].initial)


class TestForms(TestCase):
    def test_form_gets_validated(self):
        self.assertFalse(PalauteForm(data=dict(msg=None, res=None)).is_valid())
        self.assertFalse(PalauteForm(data=dict(msg='Foo', res=None)).is_valid())
        self.assertFalse(PalauteForm(data=dict(msg='Foo', res=True, email='foo')).is_valid())
        self.assertFalse(PalauteForm(data=dict(msg='Foo', res=None, email='foo@bar.fi')).is_valid())

        self.assertTrue(PalauteForm(data=dict(msg='Foo', res=True)).is_valid())
        self.assertTrue(PalauteForm(data=dict(msg='Foo', res=True, email='foo@bar.fi')).is_valid())
