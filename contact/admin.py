from django.contrib import admin
from contact.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # exibe os fields registados no model
    list_display = (
        'id', 'first_name', 'last_name', 'phone', 'email', 'created_date',
    )
    # configura a ordenação
    ordering = ('-id',)
    # disponibiliza um filtro
    list_filter = ('created_date',)
    # libera input para pesquisa
    search_fields = ('id', 'phone', 'first_name', 'last_name', )
    # limita os itens por página
    list_per_page = 15
    # limita a opção para exibir todos os registros
    list_max_show_all = 100
    # linka os inputs com seus respectivos registros
    list_display_links = 'id', 'phone',
