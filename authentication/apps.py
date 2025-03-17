"""
Módulo de configuração do app Authentication.

Este módulo define a configuração do app `authentication`, que é responsável por gerenciar
a autenticação no projeto Django. Ele configura o campo automático padrão e o nome do app.

Componentes principais:
    - AuthenticationConfig: Classe de configuração do app.

Dependências:
    - django.apps.AppConfig: Para a classe base de configuração de apps.
"""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuração do app Authentication.

    Esta classe define as configurações específicas do app `authentication`, como o campo
    automático padrão e o nome do app.

    Atributos:
        default_auto_field (str): Define o campo automático padrão para modelos (BigAutoField).
        name (str): Nome do app (authentication).
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
