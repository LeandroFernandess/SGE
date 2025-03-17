"""
Módulo de URLs para o modelo Category.

Este módulo define as URLs para as views relacionadas ao modelo Category, tanto para a interface web
quanto para a API REST. As URLs permitem listar, criar, detalhar, atualizar e excluir categorias de produtos.

Componentes principais:
    - URL para listar categorias (category_list).
    - URL para criar novas categorias (category_create).
    - URL para detalhar uma categoria específica (category_detail).
    - URL para atualizar uma categoria específica (category_update).
    - URL para excluir uma categoria específica (category_delete).
    - URL para listar e criar categorias via API (category-create-list-api-view).
    - URL para recuperar, atualizar e excluir uma categoria via API (category-detail-api-view).

Dependências:
    - django.urls.path: Para definir os padrões de URL.
    - .views: Para as views associadas às URLs.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "categories/list/",
        views.CategoryListView.as_view(),
        name="category_list",
    ),
    path(
        "categories/create/",
        views.CategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        "categories/<int:pk>/detail",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "categories/<int:pk>/update",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path(
        "api/v1/categories/",
        views.CategoryCreateListAPIView.as_view(),
        name="category-create-list-api-view",
    ),
    path(
        "api/v1/categories/<int:pk>/",
        views.CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-detail-api-view",
    ),
]
