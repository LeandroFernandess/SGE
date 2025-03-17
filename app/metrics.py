"""
Módulo de métricas para o sistema.

Este módulo define funções para calcular e retornar métricas relacionadas a produtos, vendas,
e dados diários. As métricas são usadas para gerar relatórios e gráficos na interface do sistema.

Componentes principais:
    - get_product_metrics: Calcula métricas gerais sobre os produtos.
    - get_sales_metrics: Calcula métricas relacionadas às vendas.
    - get_daily_sales_data: Retorna dados diários de vendas para gráficos.
    - get_daily_sales_quantity_data: Retorna dados diários de quantidade de vendas.
    - get_graphic_product_category_metric: Retorna a contagem de produtos por categoria.
    - get_graphic_product_brand_metric: Retorna a contagem de produtos por marca.

Dependências:
    - django.db.models: Para operações de agregação e filtragem no banco de dados.
    - django.utils: Para formatação de números e manipulação de datas.
    - products.models: Para acessar o modelo Product.
    - outflows.models: Para acessar o modelo Outflow.
    - categories.models: Para acessar o modelo Category.
    - brands.models: Para acessar o modelo Brand.
"""

from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from products.models import Product
from outflows.models import Outflow
from categories.models import Category
from brands.models import Brand


def get_product_metrics():
    """
    Calcula métricas gerais sobre os produtos.

    Esta função calcula o custo total, o preço de venda total, a quantidade total
    e o lucro total de todos os produtos no estoque.

    Retorna:
        dict: Um dicionário contendo as métricas formatadas:
            - total_cost_price: Custo total dos produtos.
            - total_selling_price: Preço de venda total dos produtos.
            - total_quantity: Quantidade total de produtos.
            - total_profit: Lucro total (venda - custo).
    """
    products = Product.objects.all()
    total_cost_price = sum(
        product.cost_price * product.quantity for product in products
    )
    total_selling_price = sum(
        product.selling_price * product.quantity for product in products
    )
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price
    return dict(
        total_cost_price=number_format(
            total_cost_price, decimal_pos=2, force_grouping=True
        ),
        total_selling_price=number_format(
            total_selling_price, decimal_pos=2, force_grouping=True
        ),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    """
    Calcula métricas relacionadas às vendas.

    Esta função calcula o total de vendas, a quantidade total de produtos vendidos,
    o valor total das vendas e o lucro total das vendas.

    Retorna:
        dict: Um dicionário contendo as métricas formatadas:
            - total_sales: Total de vendas realizadas.
            - total_product_sold: Quantidade total de produtos vendidos.
            - total_sales_value: Valor total das vendas.
            - total_sales_profit: Lucro total das vendas (venda - custo).
    """
    total_sales = Outflow.objects.count()
    total_products_sold = (
        Outflow.objects.aggregate(total_products_sold=Sum("quantity"))[
            "total_products_sold"
        ]
        or 0
    )
    total_sales_value = sum(
        outflow.quantity * outflow.product.selling_price
        for outflow in Outflow.objects.all()
    )
    total_sales_cost = sum(
        outflow.quantity * outflow.product.cost_price
        for outflow in Outflow.objects.all()
    )
    total_sales_profit = total_sales_value - total_sales_cost
    return dict(
        total_sales=total_sales,
        total_product_sold=total_products_sold,
        total_sales_value=number_format(
            total_sales_value, decimal_pos=2, force_grouping=True
        ),
        total_sales_profit=number_format(
            total_sales_profit, decimal_pos=2, force_grouping=True
        ),
    )


def get_daily_sales_data():
    """
    Retorna dados diários de vendas para gráficos.

    Esta função calcula o valor total das vendas para cada dia dos últimos 7 dias.

    Retorna:
        dict: Um dicionário contendo:
            - dates: Lista de datas dos últimos 7 dias.
            - values: Lista de valores totais de vendas para cada dia.
    """
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = (
            Outflow.objects.filter(created_at__date=date).aggregate(
                total_sales=Sum(F("product__selling_price") * F("quantity"))
            )["total_sales"]
            or 0
        )
        values.append(float(sales_total))

    return dict(dates=dates, values=values)


def get_daily_sales_quantity_data():
    """
    Retorna dados diários de quantidade de vendas.

    Esta função calcula a quantidade de vendas realizadas para cada dia dos últimos 7 dias.

    Retorna:
        dict: Um dicionário contendo:
            - dates: Lista de datas dos últimos 7 dias.
            - values: Lista de quantidades de vendas para cada dia.
    """
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(sales_quantity)

    return dict(dates=dates, values=quantities)


def get_graphic_product_category_metric():
    """
    Retorna a contagem de produtos por categoria.

    Esta função calcula a quantidade de produtos em cada categoria.

    Retorna:
        dict: Um dicionário onde as chaves são os nomes das categorias e os valores
              são a quantidade de produtos em cada categoria.
    """
    categories = Category.objects.all()
    return {
        category.name: Product.objects.filter(category=category).count()
        for category in categories
    }


def get_graphic_product_brand_metric():
    """
    Retorna a contagem de produtos por marca.

    Esta função calcula a quantidade de produtos em cada marca.

    Retorna:
        dict: Um dicionário onde as chaves são os nomes das marcas e os valores
              são a quantidade de produtos em cada marca.
    """
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}
