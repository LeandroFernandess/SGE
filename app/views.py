"""
Módulo de views para a página inicial (home).

Este módulo define a view `home`, que renderiza a página inicial do sistema. A view coleta
métricas relacionadas a produtos, vendas e dados diários, e as passa para o template.

Componentes principais:
    - home: View que renderiza a página inicial com métricas e gráficos.

Dependências:
    - json: Para serializar dados em formato JSON.
    - django.contrib.auth.decorators.login_required: Para restringir o acesso a usuários autenticados.
    - django.shortcuts.render: Para renderizar o template.
    - .metrics: Para obter as métricas e dados necessários.
"""

import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url="login")
def home(request):
    """
    View para a página inicial.

    Esta view coleta métricas relacionadas a produtos, vendas e dados diários,
    serializa os dados em formato JSON e os passa para o template `home.html`.

    Requer autenticação do usuário. Caso o usuário não esteja autenticado,
    redireciona para a página de login.

    Argumentos:
        request (HttpRequest): Objeto de requisição HTTP.

    Retorna:
        HttpResponse: Resposta HTTP que renderiza o template `home.html` com o contexto.

    Contexto:
        - product_metrics: Métricas relacionadas a produtos.
        - sales_metrics: Métricas relacionadas a vendas.
        - daily_sales_data: Dados diários de vendas em formato JSON.
        - daily_sales_quantity_data: Dados diários de quantidade de vendas em formato JSON.
        - product_count_by_category: Contagem de produtos por categoria em formato JSON.
        - product_count_by_brand: Contagem de produtos por marca em formato JSON.
    """

    # Coleta as métricas e dados
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    # Prepara o contexto para o template
    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
        "daily_sales_data": json.dumps(daily_sales_data),
        "daily_sales_quantity_data": json.dumps(daily_sales_quantity_data),
        "product_count_by_category": json.dumps(graphic_product_category_metric),
        "product_count_by_brand": json.dumps(graphic_product_brand_metric),
    }

    # Renderiza o template com o contexto
    return render(request, "home.html", context=context)
