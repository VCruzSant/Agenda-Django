from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


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
        picture = forms.ImageField(
            widget=forms.FileInput(
                attrs={
                    'accept': 'image/*'
                }
            )
        )
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture'
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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=4
    )
    last_name = forms.CharField(
        required=True,
        min_length=4
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já existe usuários com esse e-mail', code='invalid'
                )
            )
        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username'
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não são iguais')
                )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        print(self.instance)

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Já existe usuários com esse e-mail', code='invalid'
                    )
                )
            return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as e:
                self.add_error(
                    'password1',
                    ValidationError(e)
                )

        return password1
