# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

from .portfolio import portfolio


def home(request):
    context = {
        'title_page': 'Home'
    }
    return render(request, 'core/index.html', context)


def about(request):
    context = {
        'title_page': 'Quem Sou Eu'
    }
    return render(request, 'core/about.html', context)


def services(request):
    context = {
        'title_page': 'Meus Serviços'
    }
    return render(request, 'core/services.html', context)


def contact(request):
    response = {}

    if request.method == "POST":
        subject = request.POST.get('topic', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        from_name = request.POST.get('name', '')

        if subject and message and from_email and from_name:
            text = '''
                    Nome: %s \n
                    Email : %s \n
                    Mensagem: %s
            ''' % (from_name, from_email, message)

            try:
                send_mail(subject, text, from_email, ['change@this.com'])
                response['type'] = 'success'
                response['title'] = 'Ok!'
                response['message'] = 'Sua mensagem foi enviada com sucesso.'

            except:
                response['type'] = 'danger'
                response['title'] = 'Ops!'
                response['message'] = 'Sua mensagem não pode ser enviada,\
                                        tente novamente mais tarde.'

        else:
            response['type'] = 'warning'
            response['title'] = 'Atenção!'
            response['message'] = 'Preencha o formulario,\
                                    todos os campos são obrigatorio.'

    context = {
        'title_page': 'Contate-me',
        'response': response
    }
    return render(request, 'core/contact.html', context)
