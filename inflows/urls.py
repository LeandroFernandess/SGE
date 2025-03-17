"""
Módulo de URLs para o modelo Inflow.

Este módulo define as URLs para as views relacionadas ao modelo Inflow, tanto para a interface web
quanto para a API REST. As URLs permitem listar, criar e detalhar entradas de produtos (Inflows).

Componentes principais:
    - URL para listar entradas de produtos (inflow_list).
    - URL para criar novas entradas de produtos (inflow_create).
    - URL para detalhar uma entrada específica (inflow_detail).
    - URL para listar e criar entradas via API (inflow-create-list-api-view).
    - URL para recuperar detalhes de uma entrada via API (inflow-detail-api-view).

Dependências:
    - django.urls.path: Para definir os padrões de URL.
    - .views: Para as views associadas às URLs.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "inflows/list/",
        views.InflowListView.as_view(),
        name="inflow_list",
    ),
    path(
        "inflows/create/",
        views.InflowCreateView.as_view(),
        name="inflow_create",
    ),
    path(
        "inflows/<int:pk>/detail",
        views.InflowDetailView.as_view(),
        name="inflow_detail",
    ),
    path(
        "api/v1/inflows/",
        views.InflowCreateListAPIView.as_view(),
        name="inflow-create-list-api-view",
    ),
    path(
        "api/v1/inflows/<int:pk>/",
        views.InflowRetrieveAPIView.as_view(),
        name="inflow-detail-api-view",
    ),
]
