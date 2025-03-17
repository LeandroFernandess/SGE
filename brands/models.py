"""
Módulo de modelo para Brand.

Este módulo define o modelo `Brand`, que representa uma marca de produtos.
Cada marca possui um nome, uma descrição opcional e registros de data de criação e atualização.

Componentes principais:
    - Brand: Modelo que representa uma marca de produtos.

Dependências:
    - django.db.models: Para a definição dos campos e comportamentos do modelo.
"""

from django.db import models


class Brand(models.Model):
    """
    Modelo que representa uma marca de produtos.

    Este modelo registra as marcas de produtos, incluindo o nome, a descrição,
    e as datas de criação e atualização.

    Atributos:
        - name: Nome da marca (máximo de 500 caracteres).
        - description: Descrição opcional da marca.
        - created_at: Data e hora de criação da marca.
        - updated_at: Data e hora da última atualização da marca.

    Métodos:
        - __str__: Retorna uma representação legível do objeto (nome da marca).

    Meta:
        - ordering: Ordenação padrão das marcas por nome (ordem alfabética).
    """

    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """
        Retorna uma representação legível do objeto.

        Returns:
            str: Nome da marca.
        """
        return self.name
