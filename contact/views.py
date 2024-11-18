from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from contact.forms import ContactForm
from contact.models import ContactModel
from django.template.loader import render_to_string
from decouple import config

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            body = render_to_string('contact/template_contact_email.txt', {
                'name': name,
                'phone': phone,
                'email': email,
                'message': message,
            })

            # usuário
            assunto_email_usuario = "Obrigado por entrar em contato!"
            send_mail(
                assunto_email_usuario,
                body,
                config('DEFAULT_FROM_EMAIL'), #from meu email
                [email],  #to email do usuário
                fail_silently=False
            )


            # administrador
            assunto_email_admin = "Novo contato de um usuário!"
            send_mail(
                assunto_email_admin,
                body,
                config('DEFAULT_FROM_EMAIL'), #from meu email
                [config('DEFAULT_TO_EMAIL')], #to - email do eventif
                fail_silently=False 
            )
            return HttpResponse("Formulário enviado com sucesso!") 

    else:
        form = ContactForm()

    return render(request, 'contact/formulario_contact.html', {'form': form})