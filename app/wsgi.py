#!/usr/bin/env python
"""Configuração WSGI para o projeto Django.

Este módulo expõe a callable WSGI como uma variável de nível de módulo chamada `application`.

Componentes principais:
    - application: Objeto que representa a interface WSGI do projeto Django.
    - get_wsgi_application: Função que retorna a aplicação WSGI padrão do Django.

Fluxo da aplicação:
    1. Configura o módulo de configurações do Django.
    2. Obtém e disponibiliza a aplicação WSGI para o servidor.

Referências:
    - Documentação oficial: https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Define a configuração padrão do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# Obtém a aplicação WSGI
application = get_wsgi_application()
