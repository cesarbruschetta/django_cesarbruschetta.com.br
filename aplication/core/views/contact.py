# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail


def contact(request):
    response = {}

    if request.method == "POST":
        subject = request.POST.get('topic', '')
        message = request.POST.get('message', '')
        user_email = request.POST.get('email', '')
        user_name = request.POST.get('name', '')

        if subject and message and user_email and user_name:
            from_email = 'contato@cesarbruschetta.com.br'
            text = '''
                    Mensagem enviada do site \n
                    Nome: %s \n
                    Email : %s \n
                    Mensagem: %s
            ''' % (user_name, user_email, message)

            try:
                send_mail(subject, text, from_email,
                          ['cesarabruschetta@gmail.com'])

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
            response['message'] = 'Preencha o formulário,\
                                    todos os campos são obrigatório.'

    context = {
        'title_page': 'Contate-me',
        'response': response
    }
    return render(request, 'core/contact.html', context)
