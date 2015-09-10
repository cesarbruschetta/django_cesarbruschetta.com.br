
********************
Procedimento para instalar o Python 3.3.4
********************

ATENÇÂO
-------------------------

- Esta aplicação foi desenvolvida e testa para o Ubuntu 14.04, não utiliza-la em outra distribuição de linux;
- Caso opte por utilizar outar distribuição, esse procedimento de instalação não se aplica;
- Esse tutorial usa como base o diretorio /opt/, caso utilize outro diretorio, realize os ajustes necessarios;

DEPENDENCIAS
-------------------------
- Ubuntu (14.04)
    - make
    - build-essential
    - python-virtualenv
    - python-dev
    - openssl
    - libssl-dev
    - libxml2-dev
    - libxslt1.1
    - libxslt1-dev
    - lib32z1-dev

INSTALAÇÃO
-------------------------

- Para instalar as dependencias no sistema, executra o comando baixo:
    # apt-get install make build-essential python-virtualenv python-dev\
                           openssl libssl-dev libxml2-dev libxslt1.1 libxslt1-dev\
                           lib32z1-dev

- Criar o diretorio para a combilação do python:
    # mkdir -p /opt/core

- Baixar o Tar-gz do python 3.3.4 dentro da pasta /opt:
    # wget https://www.python.org/ftp/python/3.3.4/Python-3.3.4.tgz

- Descompactar o tar-gz baixado:
    # tar -xf Python-3.3.4.tgz

- Acessando a pasta descompactada, execute os comando para compilar o python:
    # ./configure --prefix=/opt/core/ && make && make install

- Apos o termino de toda a combilação, remova o tar-gz e a pasta do python 3.3.4:
    # rm -rf Python-3.3.4*