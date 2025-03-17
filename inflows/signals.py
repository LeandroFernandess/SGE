"""
Módulo de sinais para o modelo Inflow.

Este módulo define um sinal que atualiza a quantidade de um produto no estoque
sempre que uma nova entrada (Inflow) é criada.

Componentes principais:
    - update_product_quantity: Função que ajusta a quantidade do produto com base na entrada.

Dependências:
    - django.db.models.signals: Para o sinal post_save.
    - django.dispatch: Para o decorador receiver.
    - .models: Para o modelo Inflow.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    """
    Atualiza a quantidade de um produto no estoque após a criação de uma entrada.

    Esta função é disparada pelo sinal post_save do modelo Inflow. Quando uma nova entrada é criada,
    ela aumenta a quantidade do produto associado com base na quantidade da entrada.

    Argumentos:
        sender: Classe do modelo que enviou o sinal (Inflow).
        instance: Instância do modelo Inflow que foi salva.
        created: Booleano indicando se a instância foi recém-criada.
        **kwargs: Argumentos adicionais passados pelo sinal.

    Lógica:
        - Verifica se a instância foi criada (created=True).
        - Se a quantidade da entrada for maior que 0, adiciona essa quantidade ao estoque do produto.
        - Salva as alterações no produto.
    """
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()
