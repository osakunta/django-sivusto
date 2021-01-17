from django.test import TestCase
from unittest.mock import MagicMock, patch

from django.http import HttpResponseBadRequest
from django.forms.fields import CharField

from palautteet.email import EmailService
from palautteet.forms import ContactsForm
from palautteet.views import submit_form


class TestEmail(TestCase):
    def test_message_constructed(self):
        data = dict(foo='bar', fizz='buzz')
        res = EmailService._construct_message(data)
        expected = 'foo:\nbar\n\nfizz:\nbuzz'
        self.assertEqual(expected, res)

    def test_message_empty_fields_discarded(self):
        data = dict(foo='bar', fizz=None)
        res = EmailService._construct_message(data)
        expected = 'foo:\nbar'
        self.assertEqual(expected, res)


class TestForm(TestCase):
    def test_email_name_at_the_end(self):
        class AContactsForm(ContactsForm):
            myfield = CharField()

        instance = AContactsForm()
        self.assertListEqual(['name', 'email'], list(instance.fields.keys())[-2:])


class TestViews(TestCase):

    @patch('palautteet.views.render')
    def test_email_gets_sent(self, _):
        form = MagicMock()
        form.is_valid.return_value = True
        request = MagicMock()
        service = MagicMock()
        submit_form(request, form, 'foo', service)
        self.assertTrue(service.send.called)

    def test_invalid_form_responses_with_400(self):
        form = MagicMock()
        form.is_valid.return_value = False
        request = MagicMock()
        service = MagicMock()
        res = submit_form(request, form, 'foo', service)
        self.assertIsInstance(res, HttpResponseBadRequest)
