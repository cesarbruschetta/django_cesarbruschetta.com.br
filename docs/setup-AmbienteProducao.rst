
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

- Para que a rotina de atualizar o feed de noticias seja executa sempre, devemos adicionar o camando abaixo,
no crontab do servidor:

    # crontab -e
    # */30 * * * * source /root/.bashrc && source /opt/site/bin/activate && python /opt/site/app/manage.py runscript update_feeds
    * Esse comando esta configurado para executar a cada 30 minutos, esse parameto pode ser alterado,
    para isso consulte a documentação do crontab do Linux.
