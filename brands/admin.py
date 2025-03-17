"""
Módulo de administração para o modelo Brand.

Este módulo configura a interface de administração do Django para o modelo Brand,
permitindo a visualização e edição de marcas de produtos no painel de administração.

Componentes principais:
    - BrandAdmin: Classe que personaliza a exibição e a pesquisa de registros de Brand no painel de administração.

Dependências:
    - django.contrib.admin: Para o registro e configuração do modelo no painel de administração.
    - .models: Para o modelo Brand.
"""

from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    """
    Configurações de administração para o modelo Brand.

    Esta classe define como os registros de Brand são exibidos e pesquisados
    no painel de administração do Django.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de registros.
        search_fields (tuple): Campos pelos quais a pesquisa pode ser realizada.

    Exemplo de uso:
        - Exibe os campos 'name' e 'description' na lista de registros.
        - Permite a pesquisa por 'name'.
    """

    list_display = (
        "name",
        "description",
    )
    search_fields = ("name",)


# Registra o modelo Brand com a classe BrandAdmin no painel de administração
admin.site.register(models.Brand, BrandAdmin)
