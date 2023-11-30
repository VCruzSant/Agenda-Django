from django.shortcuts import render, redirect

from contact.forms import ContactForm
# Create your views here.

# request.method GET -> requisição apenas para acessar a página
# request.method POST -> requisição para enviar form
# lógica: se for POST -> Envia formulário
# lógica: se for GET -> Apenas renderiza a page


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        # se o formulário for valido-> salve na base de dados
        # .save() é a função do django
        if form.is_valid():
            # se eu quiser mudar alguma informação, eu impeço o commit
            # contact = form.save(commit=False)
            # contact.save()
            form.save()
            return redirect('contact:contact')

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
