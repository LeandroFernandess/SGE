"""
Módulo de serialização para o modelo Outflow.

Este módulo define o serializer utilizado para converter instâncias do modelo Outflow
em representações JSON e vice-versa, possibilitando a integração com APIs REST.

Componentes principais:
    - OutflowSerializer: Serializer que mapeia todos os campos do modelo Outflow.

Dependências:
    - rest_framework.serializers: Para a criação de serializers.
    - outflows.models: Para o modelo Outflow.
"""

from rest_framework import serializers
from outflows.models import Outflow


class OutflowSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Outflow.

    Converte instâncias do modelo Outflow em dados serializados (JSON) e vice-versa,
    incluindo todos os campos definidos no modelo.

    Atributos:
        Meta: Classe interna que especifica o modelo e os campos a serem serializados.
    """

    class Meta:
        model = Outflow
        fields = "__all__"
