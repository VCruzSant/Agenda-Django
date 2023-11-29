from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # atualizando o widget com update -> função python para dicts:
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Contact Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Contact Last Name',
            }
        )
        self.fields['phone'].widget.attrs.update(
            {
                'placeholder': 'Contact Phone',
            }
        )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )

        # crio widgets:
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Seu Nome'
        #         }
        #     )
        # }
    # usada para validação geral dos fields:
    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            raise ValidationError(
                'Second name cannot be the same as first name',
                code='invalid'
            )

        return super().clean()

    # usada para validação de um field específico
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'abc':
            raise ValidationError(
                'Digite um nome verdadeiro',
                code='invalid'
            )

        return first_name
