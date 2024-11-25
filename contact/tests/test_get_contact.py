from django.test import TestCase
from django.core import mail
from contact.forms import ContactForm
from contact.models import ContactModel
from django.core.mail import send_mail


class ContactGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/contact/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'contact/formulario_contact.html')

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 5),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')








