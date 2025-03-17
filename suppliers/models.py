"""
Módulo de definição do modelo Supplier.

Este módulo define o modelo Supplier para armazenar informações sobre fornecedores no banco de dados,
utilizado em diversas partes da aplicação, como views, formulários e APIs.

Componentes principais:
    - Supplier: Modelo que representa um fornecedor com campos para nome, descrição e timestamps.

Dependências:
    - django.db.models: Para a criação de modelos de banco de dados.
"""

from django.db import models


class Supplier(models.Model):
    """
    Modelo que representa um fornecedor no banco de dados.

    Armazena informações básicas sobre fornecedores, incluindo nome, descrição e datas de criação/atualização.

    Campos:
        name: Nome do fornecedor (máximo de 500 caracteres, obrigatório).
        description: Descrição detalhada do fornecedor (opcional, pode ser nulo ou vazio).
        created_at: Data e hora de criação do registro (adicionada automaticamente).
        updated_at: Data e hora da última atualização do registro (atualizada automaticamente).

    Atributos:
        Meta: Classe interna que define a ordenação padrão dos registros por nome.

    Métodos:
        __str__: Retorna o nome do fornecedor como representação em string.

    """
    
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
