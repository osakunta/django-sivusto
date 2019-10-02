from unittest import mock, TestCase

from palautteet.hallitus.utils import get_palaute_form, construct_message
from palautteet.hallitus.forms import PalauteForm, PalauteFormLogged


class TestUtils(TestCase):
    def test_right_form_returned_by_user_authentication(self):
        user = mock.MagicMock()

        user.is_authenticated = False
        res = get_palaute_form(user=user)
        self.assertIsInstance(res, PalauteForm)

        user.is_authenticated = True
        res = get_palaute_form(user=user)
        self.assertIsInstance(res, PalauteFormLogged)

    def test_initial_set(self):
        field, value = 'email', 'foo@bar.fi'

        user = mock.MagicMock()
        user.is_authenticated = True
        user.email = {field: value}

        res = get_palaute_form(user=user)
        self.assertEquals(value, res[field].initial)

    def test_message_constructed(self):
        data = dict(foo='bar', fizz='buzz')
        res = construct_message(data)
        expected = 'foo:\nbar\n\nfizz:\nbuzz'
        self.assertEquals(expected, res)


class TestForms(TestCase):
    def test_form_gets_validated(self):
        self.assertFalse(PalauteForm(data=dict(msg=None, res=None)).is_valid())
        self.assertFalse(PalauteForm(data=dict(msg='Foo', res=None)).is_valid())
        self.assertFalse(PalauteForm(data=dict(msg='Foo', res=True, email='foo')).is_valid())
        self.assertFalse(PalauteForm(data=dict(msg='Foo', res=None, email='foo@bar.fi')).is_valid())

        self.assertTrue(PalauteForm(data=dict(msg='Foo', res=True)).is_valid())
        self.assertTrue(PalauteForm(data=dict(msg='Foo', res=True, email='foo@bar.fi')).is_valid())
