"""
Módulo de administração para o modelo Product.

Este módulo configura a interface de administração do Django para o modelo Product,
permitindo gerenciar instâncias de produtos diretamente no painel admin.

Componentes principais:
    - ProductAdmin: Classe que personaliza a exibição e busca de produtos no admin.

Dependências:
    - django.contrib.admin: Para funcionalidades de administração.
    - .models: Para o modelo Product.
"""

from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    """
    Classe de administração para o modelo Product.

    Personaliza a interface de administração do Django para o modelo Product,
    definindo como os dados são exibidos e pesquisados no painel admin.

    Atributos:
        list_display: Campos exibidos na lista de produtos ("title", "serie_number").
        search_fields: Campos disponíveis para busca ("title").
    """

    list_display = ("title", "serie_number")
    search_fields = ("title",)


admin.site.register(models.Product, ProductAdmin)
