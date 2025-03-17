"""
Módulo de formulário para o modelo Product.

Este módulo define um formulário para criar e editar instâncias do modelo Product,
utilizado em views baseadas em formulários na interface web.

Componentes principais:
    - ProductForm: Formulário que mapeia campos específicos do modelo Product.

Dependências:
    - django.forms: Para a criação de formulários baseados em modelos.
    - .models: Para o modelo Product.
"""

from django import forms
from . import models


class ProductForm(forms.ModelForm):
    """
    Formulário para criar e editar instâncias do modelo Product.

    Mapeia campos específicos do modelo Product, aplicando widgets e rótulos personalizados
    para melhorar a experiência do usuário na interface web.

    Atributos:
        Meta: Classe interna que define o modelo, campos, widgets e rótulos do formulário.

    Campos:
        title: Título do produto.
        category: Categoria do produto (chave estrangeira).
        brand: Marca do produto (chave estrangeira).
        description: Descrição detalhada do produto.
        serie_number: Número de série do produto.
        cost_price: Preço de custo do produto.
        selling_price: Preço de venda do produto.

    Widgets:
        title: Campo de texto com classe "form-control".
        category: Dropdown com classe "form-control".
        brand: Dropdown com classe "form-control".
        description: Área de texto com classe "form-control" e 3 linhas.
        serie_number: Campo de texto com classe "form-control".
        cost_price: Campo numérico com classe "form-control".
        selling_price: Campo numérico com classe "form-control".

    Rótulos:
        title: "Título".
        category: "Categoria".
        brand: "Marca".
        description: "Descrição".
        serie_number: "Número de Série".
        cost_price: "Preço de Custo".
        selling_price: "Preço de Venda".

    """

    class Meta:
        model = models.Product
        fields = [
            "title",
            "category",
            "brand",
            "description",
            "serie_number",
            "cost_price",
            "selling_price",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "serie_number": forms.TextInput(attrs={"class": "form-control"}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control"}),
            "selling_price": forms.NumberInput(attrs={"class": "form-control"}),
        }
        labels = {
            "title": "Título",
            "category": "Categoria",
            "brand": "Marca",
            "description": "Descrição",
            "serie_number": "Número de Série",
            "cost_price": "Preço de Custo",
            "selling_price": "Preço de Venda",
        }
