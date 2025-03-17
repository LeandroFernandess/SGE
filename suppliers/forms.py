"""
Módulo de formulário para o modelo Supplier.

Este módulo define um formulário para criar e editar instâncias do modelo Supplier,
utilizado em views baseadas em formulários na interface web.

Componentes principais:
    - SupplierForm: Formulário que mapeia os campos "name" e "description" do modelo Supplier.

Dependências:
    - django.forms: Para a criação de formulários baseados em modelos.
    - .models: Para o modelo Supplier.
"""

from django import forms
from . import models


class SupplierForm(forms.ModelForm):
    """
    Formulário para criar e editar instâncias do modelo Supplier.

    Este formulário mapeia os campos "name" e "description" do modelo Supplier,
    aplicando widgets e rótulos personalizados para melhorar a interface do usuário.

    Atributos:
        Meta: Classe interna que define o modelo, campos, widgets e rótulos do formulário.

    Campos:
        name: Campo de texto para o nome do fornecedor.
        description: Campo de área de texto para a descrição do fornecedor.

    Widgets:
        name: Renderizado como um campo de texto com a classe CSS "form-control".
        description: Renderizado como uma área de texto com a classe CSS "form-control" e 3 linhas.

    Rótulos:
        name: Exibido como "Nome".
        description: Exibido como "Descrição".

    Exemplo de uso:
        form = SupplierForm(request.POST or None)
        if form.is_valid():
            form.save()
    """

    class Meta:
        model = models.Supplier
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "name": "Nome",
            "description": "Descrição",
        }
