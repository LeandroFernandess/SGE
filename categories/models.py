"""
Módulo de modelo para Category.

Este módulo define o modelo `Category`, que representa uma categoria de produtos.
Cada categoria possui um nome, uma descrição e registros de data de criação e atualização.

Componentes principais:
    - Category: Modelo que representa uma categoria de produtos.

Dependências:
    - django.db.models: Para a definição dos campos e comportamentos do modelo.
"""

from django.db import models


class Category(models.Model):
    """
    Modelo que representa uma categoria de produtos.

    Este modelo registra as categorias de produtos, incluindo o nome, a descrição,
    e as datas de criação e atualização.

    Atributos:
        - name: Nome da categoria (máximo de 100 caracteres).
        - description: Descrição da categoria.
        - created_at: Data e hora de criação da categoria.
        - updated_at: Data e hora da última atualização da categoria.

    Métodos:
        - __str__: Retorna uma representação legível do objeto (nome da categoria).

    Meta:
        - ordering: Ordenação padrão das categorias por nome (ordem alfabética).
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """
        Retorna uma representação legível do objeto.

        Returns:
            str: Nome da categoria.
        """
        return self.name
