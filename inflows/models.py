"""
Módulo de modelo para Inflow.

Este módulo define o modelo `Inflow`, que representa as entradas de produtos no estoque.
Cada entrada está associada a um fornecedor (Supplier) e a um produto (Product), e registra
a quantidade, uma descrição opcional, e as datas de criação e atualização.

Componentes principais:
    - Inflow: Modelo que representa uma entrada de produto no estoque.

Dependências:
    - django.db.models: Para a definição dos campos e relacionamentos do modelo.
    - suppliers.models: Para o relacionamento com o modelo Supplier.
    - products.models: Para o relacionamento com o modelo Product.
"""

from django.db import models
from suppliers.models import Supplier
from products.models import Product


class Inflow(models.Model):
    """
    Modelo que representa uma entrada de produto no estoque.

    Este modelo registra as entradas de produtos, incluindo o fornecedor, o produto,
    a quantidade, uma descrição opcional, e as datas de criação e atualização.

    Atributos:
        - supplier: Relacionamento com o modelo Supplier (chave estrangeira).
        - product: Relacionamento com o modelo Product (chave estrangeira).
        - quantity: Quantidade do produto na entrada.
        - description: Descrição opcional da entrada.
        - created_at: Data e hora de criação da entrada.
        - updated_at: Data e hora da última atualização da entrada.

    Métodos:
        - __str__: Retorna uma representação legível do objeto (nome do produto).

    Meta:
        - ordering: Ordenação padrão das entradas por data de criação (mais recente primeiro).
    """

    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name="inflows"
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="inflows"
    )
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        """
        Retorna uma representação legível do objeto.

        Returns:
            str: Nome do produto associado à entrada.
        """
        return str(self.product)
