from django.shortcuts import render

from contact.forms import ContactForm
# Create your views here.

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
