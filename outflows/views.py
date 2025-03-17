"""
Módulo de views para gerenciamento de saídas (outflows).

Este módulo contém classes de views para listar, criar e detalhar saídas (outflows),
tanto para interfaces web quanto para APIs REST. As views web requerem autenticação
e permissões específicas, enquanto as views de API fornecem endpoints para operações CRUD.

Componentes principais:
    - OutflowListView: Lista saídas com filtros e métricas adicionais.
    - OutflowCreateView: Cria uma nova saída.
    - OutflowDetailView: Exibe detalhes de uma saída.
    - OutflowCreateListAPIView: API para listar e criar saídas.
    - OutflowRetrieveAPIView: API para recuperar detalhes de uma saída.

Fluxo típico:
    1. O usuário acessa a lista de saídas com filtros opcionais.
    2. O usuário pode criar uma nova saída ou visualizar detalhes de uma existente.
    3. As APIs REST permitem listar ou recuperar saídas via endpoints.

Dependências:
    - django.contrib.auth.mixins: Para autenticação e permissões.
    - rest_framework.generics: Para views de API.
    - .models, .forms, .serializers: Modelos, formulários e serializadores locais.
    - app.metrics: Funções para métricas de vendas.
"""

from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)
from . import models, forms, serializers
from app import metrics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar saídas com paginação e filtragem.

    Exibe uma lista paginada de saídas com filtro por produto e inclui métricas de vendas
    no contexto. Requer autenticação e a permissão 'outflows.view_outflow'.

    Atributos:
        model: Modelo Outflow.
        template_name: Template HTML para renderizar a lista.
        context_object_name: Nome do objeto no contexto do template.
        paginate_by: Número de itens por página.
        permission_required: Permissão necessária para acessar a view.

    Métodos sobrescritos:
        get_queryset: Filtra o queryset com base no título do produto na query string.
        get_context_data: Adiciona métricas de vendas ao contexto do template.
    """

    model = models.Outflow
    template_name = "outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 5
    permission_required = "outflows.view_outflow"

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sales_metrics"] = metrics.get_sales_metrics()
        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar uma nova saída.

    Apresenta um formulário para criar uma saída e redireciona para a lista de saídas
    após o sucesso. Requer autenticação e a permissão 'outflows.add_outflow'.

    Atributos:
        model: Modelo Outflow.
        template_name: Template HTML para renderizar o formulário.
        form_class: Formulário usado para criar a saída.
        success_url: URL para redirecionar após a criação.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Outflow
    template_name = "outflow_create.html"
    form_class = forms.OutflowForm
    success_url = reverse_lazy("outflow_list")
    permission_required = "outflows.add_outflow"


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View para exibir detalhes de uma saída.

    Exibe informações detalhadas de uma saída específica.
    Requer autenticação e a permissão 'outflows.view_outflow'.

    Atributos:
        model: Modelo Outflow.
        template_name: Template HTML para renderizar os detalhes.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Outflow
    template_name = "outflow_detail.html"
    permission_required = "outflows.view_outflow"


class OutflowCreateListAPIView(generics.ListCreateAPIView):
    """
    API view para listar e criar saídas.

    Permite listar todas as saídas ou criar uma nova via métodos GET e POST.
    Usa o serializer OutflowSerializer para serializar os dados.

    Atributos:
        queryset: Todos os objetos Outflow.
        serializer_class: Serializer para Outflow.
    """

    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer


class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    """
    API view para recuperar detalhes de uma saída.

    Permite recuperar os detalhes de uma saída específica via método GET.
    Usa o serializer OutflowSerializer para serializar os dados.

    Atributos:
        queryset: Todos os objetos Outflow.
        serializer_class: Serializer para Outflow.
    """

    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer
