"""
Módulo de migração inicial para o modelo Product.

Este módulo define a migração inicial que cria a tabela Product no banco de dados,
estabelecendo sua estrutura com campos, chaves estrangeiras e opções de ordenação.

Componentes principais:
    - Migration: Classe que contém as operações para criar o modelo Product.

Dependências:
    - django.db.migrations: Para a definição de migrações.
    - django.db.models: Para a definição de campos do modelo.
    - django.db.models.deletion: Para configurações de exclusão em chaves estrangeiras.
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migração inicial para criar o modelo Product.

    Cria a tabela Product no banco de dados com campos para título, descrição, preços,
    quantidade e relações com Category e Brand. É a migração inicial da aplicação 'products'
    e depende das migrações iniciais de 'brands' e 'categories'.

    Atributos:
        initial: Indica que esta é a primeira migração (True).
        dependencies: Lista de migrações das quais esta depende (Brand e Category).
        operations: Lista de operações, incluindo a criação do modelo Product.

    Operações:
        - CreateModel: Cria a tabela Product com campos e opções especificadas.

    Campos do modelo:
        id: Chave primária autoincrementada (BigAutoField).
        title: Título do produto (máximo de 500 caracteres).
        description: Descrição do produto (opcional, pode ser nulo ou vazio).
        serie_number: Número de série (máximo de 200 caracteres, opcional).
        cost_price: Preço de custo (decimal com até 20 dígitos e 2 casas).
        selling_price: Preço de venda (decimal com até 20 dígitos e 2 casas).
        quantity: Quantidade em estoque (inteiro, padrão 0).
        created_at: Timestamp de criação (adicionado automaticamente).
        updated_at: Timestamp de atualização (atualizado automaticamente).
        brand: Chave estrangeira para Brand (protegida contra exclusão).
        category: Chave estrangeira para Category (protegida contra exclusão).

    Opções:
        ordering: Define a ordenação padrão por "title".
    """

    initial = True

    dependencies = [
        ("brands", "0001_initial"),
        (
            "categories",
            "0001_initial",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=500)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "serie_number",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("cost_price", models.DecimalField(decimal_places=2, max_digits=20)),
                ("selling_price", models.DecimalField(decimal_places=2, max_digits=20)),
                ("quantity", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="products",
                        to="brands.brand",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="products",
                        to="categories.category",
                    ),
                ),
            ],
            options={
                "ordering": ["title"],
            },
        ),
    ]
