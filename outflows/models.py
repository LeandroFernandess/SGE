"""
Módulo de definição do modelo Outflow.

Este módulo define o modelo Outflow para registrar saídas de produtos no banco de dados,
utilizado em diversas partes da aplicação, como views, formulários e APIs.

Componentes principais:
    - Outflow: Modelo que representa uma saída de produto com campos para quantidade, descrição, etc.

Dependências:
    - django.db.models: Para a criação de modelos de banco de dados.
    - products.models: Para o modelo Product (relação de chave estrangeira).
"""

from django.db import models
from products.models import Product


class Outflow(models.Model):
    """
    Modelo que representa uma saída de produto no banco de dados.

    Registra informações sobre saídas de produtos, incluindo o produto associado,
    quantidade retirada, descrição e timestamps de criação/atualização.

    Campos:
        product: Chave estrangeira para o modelo Product (protegida contra exclusão).
        quantity: Quantidade de itens retirados (inteiro, obrigatório).
        description: Descrição da saída (opcional, pode ser nulo ou vazio).
        created_at: Data e hora de criação do registro (adicionada automaticamente).
        updated_at: Data e hora da última atualização do registro (atualizada automaticamente).

    Atributos:
        Meta: Classe interna que define a ordenação padrão por data de criação (decrescente).

    Métodos:
        __str__: Retorna a descrição da saída como representação em string.
    """

    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="outflows"
    )
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.description
