from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        label='Mensagem', 
        required=True
    )
