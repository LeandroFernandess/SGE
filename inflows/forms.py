"""
Módulo de formulários para o modelo Inflow.

Este módulo define o formulário `InflowForm`, que é usado para criar e editar instâncias
do modelo Inflow. O formulário inclui campos personalizados com classes CSS e rótulos traduzidos.

Componentes principais:
    - InflowForm: Formulário baseado no modelo Inflow.

Dependências:
    - django.forms: Para a classe ModelForm e widgets.
    - .models: Para o modelo Inflow.
"""

from django import forms
from . import models


class InflowForm(forms.ModelForm):
    """
    Formulário para o modelo Inflow.

    Este formulário é usado para criar e editar entradas de produtos (Inflows).
    Ele inclui campos personalizados com classes CSS para estilização e rótulos traduzidos.

    Atributos da classe Meta:
        model (Model): Modelo associado ao formulário (Inflow).
        fields (list): Campos do modelo a serem incluídos no formulário.
        widgets (dict): Widgets personalizados para os campos do formulário.
        labels (dict): Rótulos personalizados para os campos do formulário.

    Campos:
        - supplier: Campo de seleção para o fornecedor.
        - product: Campo de seleção para o produto.
        - quantity: Campo de texto para a quantidade.
        - description: Campo de texto longo para a descrição.

    Personalizações:
        - Classes CSS: Os campos são estilizados com a classe "form-control".
        - Rótulos: Os rótulos dos campos são traduzidos para o português.
    """

    class Meta:
        model = models.Inflow
        fields = ["supplier", "product", "quantity", "description"]
        widgets = {
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "supplier": "Fornecedor",
            "product": "Produto",
            "description": "Descrição",
            "quantity": "Quantidade",
        }
