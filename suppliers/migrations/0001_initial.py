"""
Módulo de migração inicial para o modelo Supplier.

Este módulo define a migração inicial que cria a tabela Supplier no banco de dados,
estabelecendo a estrutura inicial do modelo com seus campos e opções.

Componentes principais:
    - Migration: Classe que contém as operações para criar o modelo Supplier.

Dependências:
    - django.db.migrations: Para a definição de migrações.
    - django.db.models: Para a definição de campos do modelo.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migração inicial para criar o modelo Supplier.

    Esta classe define a criação da tabela Supplier no banco de dados, incluindo todos
    os campos e opções de ordenação. É marcada como a migração inicial do aplicativo.

    Atributos:
        initial: Indica que esta é a primeira migração (True).
        dependencies: Lista de dependências de outras migrações (vazia neste caso).
        operations: Lista de operações a serem executadas, incluindo a criação do modelo Supplier.

    Operações:
        - CreateModel: Cria a tabela Supplier com os campos id, name, description,
          created_at e updated_at, além da opção de ordenação por nome.

    Campos do modelo:
        - id: Chave primária autoincrementada (BigAutoField).
        - name: Campo de texto com limite de 500 caracteres.
        - description: Campo de texto opcional (pode ser nulo ou vazio).
        - created_at: Timestamp de criação adicionado automaticamente.
        - updated_at: Timestamp de atualização atualizado automaticamente.

    Opções:
        - ordering: Define a ordenação padrão dos registros por "name".
    """

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
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
                ("name", models.CharField(max_length=500)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
