"""
Módulo de administração para o modelo Inflow.

Este módulo configura a interface de administração do Django para o modelo Inflow,
permitindo a visualização e edição de entradas de produtos no painel de administração.

Componentes principais:
    - InflowAdmin: Classe que personaliza a exibição e a pesquisa de registros de Inflow no painel de administração.

Dependências:
    - django.contrib.admin: Para o registro e configuração do modelo no painel de administração.
    - .models: Para o modelo Inflow.
"""

from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    """
    Configurações de administração para o modelo Inflow.

    Esta classe define como os registros de Inflow são exibidos e pesquisados
    no painel de administração do Django.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de registros.
        search_fields (tuple): Campos pelos quais a pesquisa pode ser realizada.
    """

    list_display = ("supplier", "product", "quantity", "created_at", "updated_at")
    search_fields = ("supplier__name", "product__name")


# Registra o modelo Inflow com a classe InflowAdmin no painel de administração
admin.site.register(models.Inflow, InflowAdmin)
