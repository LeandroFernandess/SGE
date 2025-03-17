"""
Módulo de formulários para o modelo Category.

Este módulo define o formulário `CategoryForm`, que é usado para criar e editar instâncias
do modelo Category. O formulário inclui campos personalizados com classes CSS e rótulos traduzidos.

Componentes principais:
    - CategoryForm: Formulário baseado no modelo Category.

Dependências:
    - django.forms: Para a classe ModelForm e widgets.
    - .models: Para o modelo Category.
"""

from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    """
    Formulário para o modelo Category.

    Este formulário é usado para criar e editar categorias de produtos.
    Ele inclui campos personalizados com classes CSS para estilização e rótulos traduzidos.

    Atributos da classe Meta:
        model (Model): Modelo associado ao formulário (Category).
        fields (list): Campos do modelo a serem incluídos no formulário.
        widgets (dict): Widgets personalizados para os campos do formulário.
        labels (dict): Rótulos personalizados para os campos do formulário.

    Campos:
        - name: Campo de texto para o nome da categoria.
        - description: Campo de texto longo para a descrição da categoria.

    Personalizações:
        - Classes CSS: Os campos são estilizados com a classe "form-control".
        - Rótulos: Os rótulos dos campos são traduzidos para o português.
    """

    class Meta:
        model = models.Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "name": "Nome",
            "description": "Descrição",
        }
