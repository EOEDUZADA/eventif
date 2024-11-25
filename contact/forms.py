from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Telefone', required=False)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        label='Mensagem', 
        required=True
    )
