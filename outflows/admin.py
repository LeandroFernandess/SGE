"""
Módulo de administração para o modelo Outflow.

Este módulo configura a interface de administração do Django para o modelo Outflow,
permitindo a visualização e edição de saídas de produtos no painel de administração.

Componentes principais:
    - OutflowAdmin: Classe que personaliza a exibição e a pesquisa de registros de Outflow no painel de administração.

Dependências:
    - django.contrib.admin: Para o registro e configuração do modelo no painel de administração.
    - .models: Para o modelo Outflow.
"""

from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    """
    Configurações de administração para o modelo Outflow.

    Esta classe define como os registros de Outflow são exibidos e pesquisados
    no painel de administração do Django.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de registros.
        search_fields (tuple): Campos pelos quais a pesquisa pode ser realizada.
    """

    list_display = (
        "product",
        "quantity",
        "created_at",
        "updated_at",
    )
    search_fields = ("product__title",)


# Registra o modelo Outflow com a classe OutflowAdmin no painel de administração
admin.site.register(models.Outflow, OutflowAdmin)
