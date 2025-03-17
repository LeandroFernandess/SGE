"""
Módulo de configuração de URLs para o gerenciamento de produtos.

Este módulo define as rotas para as views relacionadas a produtos, abrangendo tanto a interface web quanto a API REST.
Ele mapeia URLs específicas às suas respectivas views no módulo `views`.

Rotas definidas:
    - product_list: Exibe a lista de produtos na interface web.
    - product_create: Permite a criação de um novo produto na interface web.
    - product_detail: Mostra os detalhes de um produto específico na interface web.
    - product_update: Permite a atualização de um produto específico na interface web.
    - product_delete: Realiza a exclusão de um produto específico na interface web.
    - product-create-list-api-view: Endpoint da API para listar todos os produtos ou criar um novo.
    - product-detail-api-view: Endpoint da API para recuperar, atualizar ou excluir um produto específico.

Dependências:
    - django.urls: Para a definição de rotas.
    - .views: Para as classes de views associadas às rotas.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("products/list/", views.ProductListView.as_view(), name="product_list"),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/detail",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "products/<int:pk>/update",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "products/<int:pk>/delete",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "api/v1/products/",
        views.ProductCreateListAPIView.as_view(),
        name="product-create-list-api-view",
    ),
    path(
        "api/v1/products/<int:pk>/",
        views.ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product-detail-api-view",
    ),
]
