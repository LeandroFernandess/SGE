"""
Módulo de formulário para o modelo Outflow.

Este módulo define um formulário para criar e editar instâncias do modelo Outflow,
utilizado em views baseadas em formulários na interface web, com validação de quantidade.

Componentes principais:
    - OutflowForm: Formulário que mapeia campos do modelo Outflow e valida a quantidade.

Dependências:
    - django.forms: Para a criação de formulários baseados em modelos.
    - django.core.exceptions: Para a exceção ValidationError.
    - .models: Para o modelo Outflow.
"""

from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):
    """
    Formulário para criar e editar instâncias do modelo Outflow.

    Mapeia campos do modelo Outflow, aplica widgets e rótulos personalizados, e valida
    se a quantidade solicitada não excede o estoque disponível do produto.

    Atributos:
        Meta: Classe interna que define o modelo, campos, widgets e rótulos do formulário.

    Campos:
        product: Produto associado à saída (chave estrangeira).
        quantity: Quantidade de itens a serem retirados.
        description: Descrição da saída.

    Widgets:
        product: Dropdown com classe "form-control".
        quantity: Campo de texto com classe "form-control".
        description: Área de texto com classe "form-control" e 3 linhas.

    Rótulos:
        product: "Produto".
        quantity: "Quantidade".
        description: "Descrição".

    Métodos:
        clean_quantity: Valida se a quantidade não excede o estoque do produto.

    Exceções:
        ValidationError: Levantada se a quantidade for maior que o estoque disponível.
    """

    class Meta:
        model = models.Outflow
        fields = ["product", "quantity", "description"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "product": "Produto",
            "description": "Descrição",
            "quantity": "Quantidade",
        }

    def clean_quantity(self):
        """
        Valida o campo quantity para garantir que não exceda o estoque do produto.

        Recupera a quantidade e o produto dos dados validados e verifica se a quantidade
        solicitada é menor ou igual ao estoque disponível.

        Retorna:
            O valor validado de quantity.

        Levanta:
            ValidationError: Se a quantidade for maior que o estoque disponível.
        """
        quantity = self.cleaned_data.get("quantity")
        product = self.cleaned_data.get("product")
        if quantity > product.quantity:
            raise ValidationError(
                f"A quantidade disponível em estoque para o produto {product.title} é de {product.quantity} unidades."
            )
        return quantity
