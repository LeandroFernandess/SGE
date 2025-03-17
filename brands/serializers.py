"""
Módulo de serialização para o modelo Brand.

Este módulo define o serializador `BrandSerializer`, que é usado para converter instâncias
do modelo Brand em formatos como JSON e vice-versa, facilitando a integração com APIs REST.

Componentes principais:
    - BrandSerializer: Serializador para o modelo Brand.

Dependências:
    - rest_framework.serializers: Para a classe ModelSerializer.
    - brands.models: Para o modelo Brand.
"""

from rest_framework import serializers
from brands.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Brand.

    Este serializador converte instâncias do modelo Brand em representações JSON
    e valida dados recebidos para criação ou atualização de marcas.

    Atributos da classe Meta:
        model (Model): Modelo associado ao serializador (Brand).
        fields (str): Campos do modelo a serem incluídos na serialização.
                      Usando "__all__", todos os campos do modelo são serializados.
    """

    class Meta:
        model = Brand
        fields = "__all__"
