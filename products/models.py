"""
Módulo de definição do modelo Product.

Este módulo define o modelo Product para armazenar informações sobre produtos no banco de dados,
utilizado em diversas partes da aplicação, como views, formulários e APIs.

Componentes principais:
    - Product: Modelo que representa um produto com campos para título, categoria, marca, preços, etc.

Dependências:
    - django.db.models: Para a criação de modelos de banco de dados.
    - categories.models: Para o modelo Category (relação de chave estrangeira).
    - brands.models: Para o modelo Brand (relação de chave estrangeira).
"""

from django.db import models
from categories.models import Category
from brands.models import Brand


class Product(models.Model):
    """
    Modelo que representa um produto no banco de dados.

    Armazena informações detalhadas sobre produtos, como título, categoria, marca, preços,
    quantidade e timestamps de criação/atualização.

    Campos:
        title: Título do produto (máximo de 500 caracteres, obrigatório).
        category: Chave estrangeira para o modelo Category (protegida contra exclusão).
        brand: Chave estrangeira para o modelo Brand (protegida contra exclusão).
        description: Descrição detalhada do produto (opcional, pode ser nulo ou vazio).
        serie_number: Número de série do produto (máximo de 200 caracteres, opcional).
        cost_price: Preço de custo do produto (decimal com até 20 dígitos e 2 casas).
        selling_price: Preço de venda do produto (decimal com até 20 dígitos e 2 casas).
        quantity: Quantidade em estoque (inteiro, padrão é 0).
        created_at: Data e hora de criação do registro (adicionada automaticamente).
        updated_at: Data e hora da última atualização do registro (atualizada automaticamente).

    Atributos:
        Meta: Classe interna que define a ordenação padrão dos registros por título.

    Métodos:
        __str__: Retorna o título do produto como representação em string.

    """

    title = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
