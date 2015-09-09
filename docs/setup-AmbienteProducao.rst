
********************
Procedimento para configurar ambinete de produção
********************

ATENÇÂO
-------------------------

- Esta aplicação foi desenvolvida e testa para o Ubuntu 14.04, não utiliza-la em outra distribuição de linux;
- Caso opte por utilizar outar distribuição, esse procedimento de instalação não se aplica;
- Esse tutorial depende que todos os passos do tutorial "Install-Aplicacao.rst" tenha sido realizados;

Tarefas Agendas
-------------------------

- Criar os scripts para o crontab:
    # echo  > /root/update_feeds.sh
    # echo  > /root/remove_oldnews.sh

- Adicionar ao arquivo '/root/update_feeds.sh' o camando abaixo:
    #! /bin/bash
    /opt/site/bin/python /opt/site/app/manage.py runscript update_feeds

- Adicionar ao arquivo '/root/remove_oldnews.sh' o camando abaixo:
    #! /bin/bash
    /opt/site/bin/python /opt/site/app/manage.py runscript remove_oldnews

- Atribuir permissao de execução aos scripts criados:
    # chmod +x /root/update_feeds.sh
    # chmod +x /root/remove_oldnews.sh

- Para que a rotina de atualizar o feed de noticias seja executa sempre, devemos adicionar o camando abaixo,
no crontab do servidor:

    # crontab -e
    # */30 * * * * /root/update_feeds.sh
    #   0  1 1 * * /root/remove_oldnews.sh
    * O primeiro comando esta configurado para executar a cada 30 minutos,
    * O segundo comando esta configurado para executar no 1º dia de cada mes a 1 da manha,
    Esses parametos pode ser alterados, para isso consulte a documentação do crontab do Linux.
