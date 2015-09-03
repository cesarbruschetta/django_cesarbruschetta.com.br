
********************
Procedimento para instalar a aplicação
********************


ATENÇÂO
-------------------------

- Esta aplicação foi desenvolvida e testa para o Ubuntu 14.04, não utiliza-la em outra distribuição de linux;
- Caso opte por utilizar outar distribuição, esse procedimento de instalação não se aplica;
- Esse tutorial usa como base o diretorio /opt/site, caso utilize outro diretorio, realize os ajustes necessarios;

DEPENDENCIAS
-------------------------
- Ubuntu (14.04)
    - mysql-server
    - libmysqlclient-dev
    - memcached
    - git-core

INSTALAÇÃO
-------------------------

- Para instalar as dependencias no sistema, executra o comando baixo:
    # apt-get install mysql-server libmysqlclient-dev memcached git-core

- Criar a Base de dados para a aplicação:
    # mysql -u root -p -e "CREATE DATABASE sitecesar;"

- Criação do usuario para acessar so a base de dados da aplicação:
    # mysql -u root -p -e "CREATE USER 'sitecesar'@'localhost' IDENTIFIED BY '45a78b';"
    # mysql -u root -p -e "GRANT ALL PRIVILEGES ON sitecesar. * TO 'sitecesar'@'localhost';"

    * LEMBRE-SE: o nome do banco de dados, nome do usuario, senha do usuario, podem ser modificamos,
    mas essas alterações devem ser replicadas na etapa de configuração da aplicação

- Para criar o virtualenv da aplicação:
    # /opt/core/bin/pyvenv site

- Acessando a pasta do virtualenv criado, baixar o pip:
    # wget https://bootstrap.pypa.io/get-pip.py

- Executar o get-pip.py:
    # ./bin/python get-pip.py

- Clonar o repositorio git da aplicação:
    # git clone https://bitbucket.org/cesarbruschetta/site_cesarbruschetta.com.br.git app

- Acessando a pasta da aplicação clonada, executar a instalação das dependencias da aplicação:
    # ../bin/pip install -r requirements.txt

- Para configurar a aplicação com os parametros locais do ambiente, crie um arquivo chamado 'custom_settings.py'  dentro da pastas 'aplication':
    # echo  > aplication/custom_settings.py

- Nesse arquivo iremos colocar as configurações do banco de dados, como mostrado abaixo:
    from .settings import DATABASES
    DATABASES['default']['USER'] = 'sitecesar'
    DATABASES['default']['PASSWORD'] = '45a78b'

    * caso tenha mudado o nome do banco de dados, deve-se adicinar o parametro para o nome do banco, como abaixo:
        DATABASES['default']['NAME'] = 'XXXXXX'

- Apos a configuração do ambinete devemos rodar o camando para criar as tabelas do banco de dados:
    # ../bin/python ./manage.py migrate

- Agora devemos criar o super-usuario para acessar o admin da aplicação:
    # ../bin/python ./manage.py createsuperuser

    * esse comando ira solicitar o nome do usuariio, email e uma senha, como mostrado abaixo:
    Username (leave blank to use 'root'): admin
    Email address: admin@admin.com
    Password: ******
    Password (again): ******
    Superuser created successfully.

- Agora devemos iniciar o servidor web de teste, com o camando abaixo:
    # ../bin/python ./manage.py runserver 0.0.0.0:8000

- Apos isso, podemos testar atraves do seu navegador se a aplicação esta funcionando perfeitamente,
  acessando no navegador o endereço: http://IP-DO-SERVIDOR:8000/
