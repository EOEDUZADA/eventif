from django.db import models


# Create your models here.

class ContactModel(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    message = models.TextField('mensagem')
    reply = models.TextField('resposta', blank=True)
    reply_date = models.DateTimeField('foi respondido em', blank=True, null=True)
    replied = models.BooleanField('respondido', default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


