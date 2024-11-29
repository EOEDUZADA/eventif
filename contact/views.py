from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from contact.forms import ContactForm
from contact.models import ContactModel
from django.template.loader import render_to_string
from decouple import config
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)


    if not form.is_valid():
        return render(request, 'contact/formulario_contact.html', {'form': form})

    # Lista de destinatários
    to_emails = [
        form.cleaned_data['email'],  # Email do usuário
        settings.DEFAULT_TO_EMAIL    # Email do eventif
    ]

    # Envia o email 
    _send_mail(
        'contact/template_contact_email.txt',
        form.cleaned_data,
        'Obrigado por entrar em contato!',
        config('EMAIL_HOST_USER'),
        to_emails  # tupla com os destinatarios
    )

    ContactModel.objects.create(**form.cleaned_data)

    # mensagem de sucess
    messages.success(request, 'Contato enviado com sucesso!')
    return HttpResponseRedirect('/contact/')

def new(request):
    return render(request, 'contact/formulario_contact.html', {'form': ContactForm()})

def _send_mail(template_name, context, subject, from_email, to_emails):
    body = render_to_string(template_name, context)
    send_mail(
        subject,  # Assunto
        body,     # (template)
        from_email,  # quem envia
        to_emails,  # quem recebe o email
        fail_silently=False  # Se falhar, irá lançar um erro
    )