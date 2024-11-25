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


class ContactEmailPostValid(TestCase):
    def setUp(self):
        data = dict(name="Eduardo Silva", email='duduzada123@gmail.com', phone='53-12345-6789',
        message='Teste de Email!')
        self.client.post('/contact/', data)
        self.email = mail.outbox[0]
    def test_contact_email_subject(self):
        expect = 'Obrigado por entrar em contato!'
        self.assertEqual(expect, self.email.subject)
    def test_contact_email_from(self):
        expect = 'eduardo.silva@aluno.riogrande.ifrs.edu.br' #TROCAR
        self.assertEqual(expect, self.email.from_email)
    def test_contact_email_to(self):
        expect = ['duduzada123@gmail.com'] # TROCAR
        self.assertEqual(expect, self.email.to)
    def test_contact_email_body(self):
        contents = (
            'Eduardo Silva',
            '53-12345-6789',
            'duduzada123@gmail.com',
            'Teste de Email!'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)




