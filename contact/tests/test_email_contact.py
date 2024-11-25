from django.test import TestCase
from django.core import mail
from django.core.mail import send_mail

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
