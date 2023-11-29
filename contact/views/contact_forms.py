from django import forms
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from contact.models import Contact
# Create your views here.


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Menssage Error',
                code='invalid'
            )
        )

        return super().clean()

# request.method GET -> requisição apenas para acessar a página
# request.method POST -> requisição para enviar form
# lógica: se for POST -> Envia formulário
# lógica: se for GET -> Apenas renderiza a page


def create(request):
    if request.method == 'POST':
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))

        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )
