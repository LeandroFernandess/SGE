"""
Módulo de migração para o modelo Outflow.

Este módulo define a migração inicial para o modelo Outflow, que representa as saídas de produtos.
A migração cria a tabela no banco de dados com os campos necessários e define o relacionamento
com o modelo Product.

Componentes principais:
    - Migration: Classe que define a migração, herdando de `django.db.migrations.Migration`.
    - CreateModel: Operação que cria o modelo Outflow no banco de dados.

Dependências:
    - django.db.migrations: Para a criação e gerenciamento de migrações.
    - django.db.models: Para a definição dos campos do modelo.
    - products: Para o relacionamento com o modelo Product.
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Classe de migração para o modelo Outflow.

    Esta classe define a migração inicial para o modelo Outflow, incluindo a criação da tabela
    no banco de dados e a definição dos campos e relacionamentos.

    Atributos:
        initial (bool): Indica que esta é a migração inicial para o modelo.
        dependencies (list): Lista de dependências de outras migrações.
        operations (list): Lista de operações a serem executadas durante a migração.

    Operações:
        - CreateModel: Cria o modelo Outflow com os campos:
            - id: Chave primária automática.
            - quantity: Quantidade do produto na saída.
            - description: Descrição opcional da saída.
            - created_at: Data e hora de criação.
            - updated_at: Data e hora da última atualização.
            - product: Relacionamento com o modelo Product.
    """

    initial = True

    dependencies = [
        (
            "products",
            "0001_initial",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Outflow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="outflows",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
