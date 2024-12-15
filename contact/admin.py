from django.contrib import admin
from django.utils.timezone import now
from contact.models import ContactModel
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime
from decouple import config

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'reply','reply_date', 'replied',
                    'created_at', 'contacted_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'message', 'created_at')
    list_filter = ('created_at',)

    def contacted_today(self, obj):
        return obj.created_at.date() == now().date()

    contacted_today.short_description = 'Contato feito hoje?'
    contacted_today.boolean = True


admin.site.register(ContactModel, ContactModelAdmin)


# Django Signals
@receiver(post_save, sender=ContactModel)
def enviar_email_resposta(sender, instance, created, **kwargs):

    if not created and instance.replied and instance.reply:
      
        subject = f"Resposta do seu contato com o Eventif"
        
        body = render_to_string('contact/contact_response.txt', {
            'name': instance.name,
            'phone': instance.phone,
            'email': instance.email,
            'message': instance.message,
            'response': instance.reply,
        })

        to_emails = [
        instance.email,  # Email do usuário
        settings.DEFAULT_TO_EMAIL  # Email do eventif
    ]
        
        send_mail(
            subject,  # assunto
            body,  # renderizado do template passado
            config('EMAIL_HOST_USER'), # quem envia(vai estar no config do env)
            to_emails,  # quem recebe
            fail_silently=False,
        )