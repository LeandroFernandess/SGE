"""
Módulo de serialização para o modelo Supplier.

Este módulo define o serializer utilizado para converter instâncias do modelo Supplier
em representações JSON e vice-versa, facilitando a integração com APIs REST.

Componentes principais:
    - SupplierSerializer: Serializer que mapeia todos os campos do modelo Supplier.

Dependências:
    - rest_framework.serializers: Para a criação de serializers.
    - suppliers.models: Para o modelo Supplier.
"""

from rest_framework import serializers
from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Supplier.

    Este serializer converte instâncias do modelo Supplier em dados serializados (JSON)
    e vice-versa, incluindo todos os campos do modelo.

    Atributos:
        Meta: Classe interna que define o modelo e os campos a serem serializados.

    Exemplo de uso:
        serializer = SupplierSerializer(supplier_instance)
        data = serializer.data  # Dados serializados
    """

    class Meta:
        model = Supplier
        fields = "__all__"
