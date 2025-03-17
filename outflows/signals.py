"""
Módulo de sinais para o modelo Outflow.

Este módulo define um sinal que atualiza a quantidade de um produto no estoque
sempre que uma nova saída (Outflow) é criada.

Componentes principais:
    - update_product_quantity: Função que ajusta a quantidade do produto com base na saída.

Dependências:
    - django.db.models.signals: Para o sinal post_save.
    - django.dispatch: Para o decorador receiver.
    - .models: Para o modelo Outflow.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    """
    Atualiza a quantidade de um produto no estoque após a criação de uma saída.

    Esta função é disparada pelo sinal post_save do modelo Outflow. Quando uma nova saída é criada,
    ela reduz a quantidade do produto associado com base na quantidade da saída.

    Argumentos:
        sender: Classe do modelo que enviou o sinal (Outflow).
        instance: Instância do modelo Outflow que foi salva.
        created: Booleano indicando se a instância foi recém-criada.
        **kwargs: Argumentos adicionais passados pelo sinal.

    Lógica:
        - Verifica se a instância foi criada (created=True).
        - Se a quantidade da saída for maior que 0, subtrai essa quantidade do estoque do produto.
        - Salva as alterações no produto.
    """
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()
