"""
Módulo de serialização para o modelo Category.

Este módulo define o serializador `CategorySerializer`, que é usado para converter instâncias
do modelo Category em formatos como JSON e vice-versa, facilitando a integração com APIs REST.

Componentes principais:
    - CategorySerializer: Serializador para o modelo Category.

Dependências:
    - rest_framework.serializers: Para a classe ModelSerializer.
    - categories.models: Para o modelo Category.
"""

from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Category.

    Este serializador converte instâncias do modelo Category em representações JSON
    e valida dados recebidos para criação ou atualização de categorias de produtos.

    Atributos da classe Meta:
        model (Model): Modelo associado ao serializador (Category).
        fields (str): Campos do modelo a serem incluídos na serialização.
                      Usando "__all__", todos os campos do modelo são serializados.
    """

    class Meta:
        model = Category
        fields = "__all__"
