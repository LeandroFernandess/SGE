"""
Módulo de configuração de URLs para o gerenciamento de saídas (outflows).

Este módulo define as rotas para as views relacionadas a saídas, abrangendo tanto a interface web
quanto a API REST. Ele mapeia URLs específicas às suas respectivas views no módulo `views`.

Rotas definidas:
    - outflow_list: Exibe a lista de saídas na interface web.
    - outflow_create: Permite a criação de uma nova saída na interface web.
    - outflow_detail: Mostra os detalhes de uma saída específica na interface web.
    - outflow-create-list-api-view: Endpoint da API para listar todas as saídas ou criar uma nova.
    - outflow-detail-api-view: Endpoint da API para recuperar os detalhes de uma saída específica.

Dependências:
    - django.urls: Para a definição de rotas.
    - .views: Para as classes de views associadas às rotas.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("outflows/list/", views.OutflowListView.as_view(), name="outflow_list"),
    path("outflows/create/", views.OutflowCreateView.as_view(), name="outflow_create"),
    path(
        "outflows/<int:pk>/detail",
        views.OutflowDetailView.as_view(),
        name="outflow_detail",
    ),
    path(
        "api/v1/outflows/",
        views.OutflowCreateListAPIView.as_view(),
        name="outflow-create-list-api-view",
    ),
    path(
        "api/v1/outflows/<int:pk>/",
        views.OutflowRetrieveAPIView.as_view(),
        name="outflow-detail-api-view",
    ),
]
