# Eventex

Sistema de Eventos encomendado pela Morena.
[![Build Status](https://travis-ci.org/AntonioThomazinho/wttd.svg?branch=master)](https://travis-ci.org/AntonioThomazinho/wttd)
[![Maintainability](https://api.codeclimate.com/v1/badges/4ddd454fcd240651b698/maintainability)](https://codeclimate.com/github/AntonioThomazinho/wttd/maintainability)
## Como desenvolver?

1. Clone o respositório
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/AntonioThomazinho/wttd.git wttd
cd wttd
pyhton -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstância
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```



 

