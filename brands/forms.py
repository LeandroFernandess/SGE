"""
Módulo de formulários para o modelo Brand.

Este módulo define o formulário `BrandForm`, que é usado para criar e editar instâncias
do modelo Brand. O formulário inclui campos personalizados com classes CSS e rótulos traduzidos.

Componentes principais:
    - BrandForm: Formulário baseado no modelo Brand.

Dependências:
    - django.forms: Para a classe ModelForm e widgets.
    - .models: Para o modelo Brand.
"""

from django import forms
from . import models


class BrandForm(forms.ModelForm):
    """
    Formulário para o modelo Brand.

    Este formulário é usado para criar e editar marcas de produtos.
    Ele inclui campos personalizados com classes CSS para estilização e rótulos traduzidos.

    Atributos da classe Meta:
        model (Model): Modelo associado ao formulário (Brand).
        fields (list): Campos do modelo a serem incluídos no formulário.
        widgets (dict): Widgets personalizados para os campos do formulário.
        labels (dict): Rótulos personalizados para os campos do formulário.

    Campos:
        - name: Campo de texto para o nome da marca.
        - description: Campo de texto longo para a descrição da marca.

    Personalizações:
        - Classes CSS: Os campos são estilizados com a classe "form-control".
        - Rótulos: Os rótulos dos campos são traduzidos para o português.
    """

    class Meta:
        model = models.Brand
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "name": "Nome",
            "description": "Descrição",
        }
