from django.test import TestCase
from django.core import mail
from contact.forms import ContactForm
from contact.models import ContactModel
from django.core.mail import send_mail

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Eduardo Silva",
                    email='eduardo.silva@aluno.riogrande.ifrs.edu.br', phone='53-12345-6789', message='Teste de post')
        self.resp = self.client.post('/contact/', data)

    def test_post(self):
        self.assertRedirects(self.resp, '/contact/')


    def test_send_contact_email(self):
        self.assertEqual(2, len(mail.outbox))

    def test_save_contact(self):
        self.assertTrue(ContactModel.objects.exists())


class ContactPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contact/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/formulario_contact.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_contact(self):
        self.assertFalse(ContactModel.objects.exists())