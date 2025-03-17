"""
Módulo de serialização para o modelo Inflow.

Este módulo define o serializador `InflowSerializer`, que é usado para converter instâncias
do modelo Inflow em formatos como JSON e vice-versa, facilitando a integração com APIs REST.

Componentes principais:
    - InflowSerializer: Serializador para o modelo Inflow.

Dependências:
    - rest_framework.serializers: Para a classe ModelSerializer.
    - inflows.models: Para o modelo Inflow.
"""

from rest_framework import serializers
from inflows.models import Inflow


class InflowSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Inflow.

    Este serializador converte instâncias do modelo Inflow em representações JSON
    e valida dados recebidos para criação ou atualização de entradas de produtos.

    Atributos da classe Meta:
        model (Model): Modelo associado ao serializador (Inflow).
        fields (str): Campos do modelo a serem incluídos na serialização.
                      Usando "__all__", todos os campos do modelo são serializados.
    """

    class Meta:
        model = Inflow
        fields = "__all__"
