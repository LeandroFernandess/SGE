"""Módulo de configuração de aplicativos do Django.

Este módulo fornece a classe AppConfig, que é usada para configurar uma aplicação Django.

Componentes principais:
    - AppConfig: Classe base para configurar uma aplicação Django.

Descrição:
    Este módulo permite definir configurações específicas para uma aplicação Django, como o nome da
    aplicação e o tipo de campo padrão para chaves primárias. É uma parte fundamental do ciclo de
    vida de uma aplicação Django.
"""

from django.apps import AppConfig


class BrandsConfig(AppConfig):
    """Configuração da aplicação de marcas.

    Esta classe define a configuração da aplicação 'brands', incluindo a definição do campo
    padrão para chaves primárias.

    Atributos:
        - default_auto_field: Define o tipo de campo padrão para chaves primárias (BigAutoField).
        - name: Nome da aplicação (brands).
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "brands"
