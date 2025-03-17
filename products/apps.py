"""
Módulo de configuração da aplicação Products.

Este módulo define a configuração da aplicação 'products' no Django,
especificando opções como o tipo de campo automático padrão para chaves primárias.

Componentes principais:
    - ProductsConfig: Classe de configuração da aplicação Products.

Dependências:
    - django.apps: Para a criação de configurações de aplicações.
"""

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Classe de configuração para a aplicação Products.

    Define as configurações específicas da aplicação 'products', como o tipo de campo
    automático usado para chaves primárias e o nome da aplicação.

    Atributos:
        default_auto_field: Tipo de campo automático padrão para chaves primárias (BigAutoField).
        name: Nome da aplicação no projeto Django ("products").
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
