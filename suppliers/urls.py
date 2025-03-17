"""
Módulo de configuração de URLs para o gerenciamento de fornecedores.

Este módulo define as rotas para as views relacionadas a fornecedores, abrangendo tanto a interface web quanto a API REST. 
Ele é responsável por mapear URLs específicas às suas respectivas views no módulo `views`.

Rotas definidas:
    - supplier_list: Exibe a lista de fornecedores na interface web.
    - supplier_create: Permite a criação de um novo fornecedor na interface web.
    - supplier_detail: Mostra os detalhes de um fornecedor específico na interface web.
    - supplier_update: Permite a atualização de um fornecedor específico na interface web.
    - supplier_delete: Realiza a exclusão de um fornecedor específico na interface web.
    - supplier-create-list-api-view: Endpoint da API para listar todos os fornecedores ou criar um novo.
    - supplier-detail-api-view: Endpoint da API para recuperar, atualizar ou excluir um fornecedor específico.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("suppliers/list/", views.SupplierListView.as_view(), name="supplier_list"),
    path(
        "suppliers/create/", views.SupplierCreateView.as_view(), name="supplier_create"
    ),
    path(
        "suppliers/<int:pk>/detail/",
        views.SupplierDetailView.as_view(),
        name="supplier_detail",
    ),
    path(
        "suppliers/<int:pk>/update/",
        views.SupplierUpdateView.as_view(),
        name="supplier_update",
    ),
    path(
        "suppliers/<int:pk>/delete/",
        views.SupplierDeleteView.as_view(),
        name="supplier_delete",
    ),
    path(
        "api/v1/suppliers/",
        views.SupplierCreateListAPIView.as_view(),
        name="supplier-create-list-api-view",
    ),
    path(
        "api/v1/suppliers/<int:pk>/",
        views.SupplierRetrieveUpdateDestroyAPIView.as_view(),
        name="supplier-detail-api-view",
    ),
]
