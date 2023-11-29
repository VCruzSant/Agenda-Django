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
            'first_name', 'last_name', 'phone'
        )

        # crio widgets:
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Seu Nome'
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Menssage Error',
                code='invalid'
            )
        )

        self.add_error(
            'last_name',
            ValidationError(
                'Menssage Error',
                code='invalid'
            )
        )

        self.add_error(
            'phone',
            ValidationError(
                'Menssage Error',
                code='invalid'
            )
        )

        return super().clean()
