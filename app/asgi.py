#!/usr/bin/env python
"""Configuração ASGI para o projeto Django.

Este módulo expõe a callable ASGI como uma variável de nível de módulo chamada `application`.

Componentes principais:
    - application: Objeto que representa a interface ASGI do projeto Django.

Fluxo da aplicação:
    1. Configura o módulo de configurações do Django.
    2. Obtém e disponibiliza a aplicação ASGI para o servidor.

Referências:
    - Documentação oficial: https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Define a configuração padrão do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

# Obtém a aplicação ASGI
application = get_asgi_application()
