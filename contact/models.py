from django.db import models
from django.utils import timezone

# Create your models here.

# model gerencia as migrations


class Contact(models.Model):
    # Field -> campos
    # CharField -> campo que limita caracteres
    # blank = True -> parametro que torna o campo opicional
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    # pega a data no momento em que um contato é criado:
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    # Com isso, consigo alterar o contact name que é exibido
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
