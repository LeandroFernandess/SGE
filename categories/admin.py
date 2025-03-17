"""
Módulo de administração para o modelo Category.

Este módulo configura a interface de administração do Django para o modelo Category,
permitindo a visualização e edição de categorias de produtos no painel de administração.

Componentes principais:
    - CategoryAdmin: Classe que personaliza a exibição e a pesquisa de registros de Category no painel de administração.

Dependências:
    - django.contrib.admin: Para o registro e configuração do modelo no painel de administração.
    - .models: Para o modelo Category.
"""

from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    """
    Configurações de administração para o modelo Category.

    Esta classe define como os registros de Category são exibidos e pesquisados
    no painel de administração do Django.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de registros.
        search_fields (tuple): Campos pelos quais a pesquisa pode ser realizada.

    Exemplo de uso:
        - Exibe os campos 'name' e 'description' na lista de registros.
        - Permite a pesquisa por 'name'.
    """

    list_display = ("name", "description")
    search_fields = ("name",)


# Registra o modelo Category com a classe CategoryAdmin no painel de administração
admin.site.register(models.Category, CategoryAdmin)
