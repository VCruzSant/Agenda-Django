from django.shortcuts import render
from contact.models import Contact
# Create your views here.


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    # imprime, no console, a query que está sendo executada:
    print(contacts.query)

    context = {
        'contacts': contacts
    }
    return render(
        request,
        'contact/index.html',
        context
    )
