"""
Módulo de administração para o modelo Supplier.

Este módulo configura a interface de administração do Django para o modelo Supplier,
permitindo gerenciar instâncias de fornecedores diretamente no painel admin.

Componentes principais:
    - SupplierAdmin: Classe que personaliza a exibição e busca de fornecedores no admin.

Dependências:
    - django.contrib.admin: Para funcionalidades de administração.
    - .models: Para o modelo Supplier.
"""

from django.contrib import admin
from . import models


class SupplierAdmin(admin.ModelAdmin):
    """
    Classe de administração para o modelo Supplier.

    Personaliza a interface de administração do Django para o modelo Supplier,
    definindo como os dados são exibidos e pesquisados.

    Atributos:
        list_display: Campos exibidos na lista de fornecedores ("name", "description").
        search_fields: Campos disponíveis para busca ("name").

    Exemplo de uso:
        Acesse /admin/suppliers/supplier/ para listar, editar ou adicionar fornecedores.
    """

    list_display = ("name", "description")
    search_fields = ("name",)


admin.site.register(models.Supplier, SupplierAdmin)
