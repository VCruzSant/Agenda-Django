from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact
# Create your views here.

# request.method GET -> requisição apenas para acessar a página
# request.method POST -> requisição para enviar form
# lógica: se for POST -> Envia formulário
# lógica: se for GET -> Apenas renderiza a page


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # se o formulário for valido-> salve na base de dados
        # .save() é a função do django
        if form.is_valid():
            # se eu quiser mudar alguma informação, eu impeço o commit
            # contact = form.save(commit=False)
            # contact.save()

            # dessa forma eu consigo passar o que foi salvo
            # assim eu extraio o contact.pk -> primory key que é o ID
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    form = ContactForm()

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def update(request, contact_id):
    # ou pega os dados dos contatos, id e que esteja com show
    # ou retorne 404
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    # redireciona pra página de update com o id do contato
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        # formulário instanciado com dados do contato
        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # se o formulário for valido-> salve na base de dados
        # .save() é a função do django
        if form.is_valid():
            # se eu quiser mudar alguma informação, eu impeço o commit
            # contact = form.save(commit=False)
            # contact.save()

            # dessa forma eu consigo passar o que foi salvo
            # assim eu extraio o contact.pk -> primory key que é o ID
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    form = ContactForm(instance=contact)

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    # Na requisição, pegue o valor confirmation
    # e se não tiver valor, confirmation vai ser no
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )
