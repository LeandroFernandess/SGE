"""
Módulo de URLs para o modelo Brand.

Este módulo define as URLs para as views relacionadas ao modelo Brand, tanto para a interface web
quanto para a API REST. As URLs permitem listar, criar, detalhar, atualizar e excluir marcas.

Componentes principais:
    - URL para listar marcas (brand_list).
    - URL para criar novas marcas (brand_create).
    - URL para detalhar uma marca específica (brand_detail).
    - URL para atualizar uma marca específica (brand_update).
    - URL para excluir uma marca específica (brand_delete).
    - URL para listar e criar marcas via API (brand-create-list-api-view).
    - URL para recuperar, atualizar e excluir uma marca via API (brand-detail-api-view).

Dependências:
    - django.urls.path: Para definir os padrões de URL.
    - .views: Para as views associadas às URLs.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Rota para listar marcas
    path("brands/list/", views.BrandListView.as_view(), name="brand_list"),
    # Rota para criar novas marcas
    path("brands/create/", views.BrandCreateView.as_view(), name="brand_create"),
    # Rota para detalhar uma marca específica
    path(
        "brands/<int:pk>/detail",
        views.BrandDetailView.as_view(),
        name="brand_detail",
    ),
    # Rota para atualizar uma marca específica
    path(
        "brands/<int:pk>/update",
        views.BrandUpdateView.as_view(),
        name="brand_update",
    ),
    # Rota para excluir uma marca específica
    path(
        "brands/<int:pk>/delete",
        views.BrandDeleteView.as_view(),
        name="brand_delete",
    ),
    # Rota para listar e criar marcas via API
    path(
        "api/v1/brands/",
        views.BrandCreateListAPIView.as_view(),
        name="brand-create-list-api-view",
    ),
    # Rota para recuperar, atualizar e excluir uma marca via API
    path(
        "api/v1/brands/<int:pk>/",
        views.BrandRetrieveUpdateDestroyAPIView.as_view(),
        name="brand-detail-api-view",
    ),
]
