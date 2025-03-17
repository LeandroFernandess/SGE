"""
Módulo de serialização para o modelo Product.

Este módulo define o serializer utilizado para converter instâncias do modelo Product
em representações JSON e vice-versa, possibilitando a integração com APIs REST.

Componentes principais:
    - ProductSerializer: Serializer que mapeia todos os campos do modelo Product.

Dependências:
    - rest_framework.serializers: Para a criação de serializers.
    - products.models: Para o modelo Product.
"""

from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Product.

    Converte instâncias do modelo Product em dados serializados (JSON) e vice-versa,
    incluindo todos os campos definidos no modelo.

    Atributos:
        Meta: Classe interna que especifica o modelo e os campos a serem serializados.

    Exemplo de uso:
        serializer = ProductSerializer(product_instance)
        data = serializer.data  # Obtém os dados serializados em JSON
    """

    class Meta:
        model = Product
        fields = "__all__"
