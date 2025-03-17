"""
Módulo de views para o modelo Inflow.

Este módulo define as views baseadas em classes para listar, criar, detalhar e interagir
com o modelo Inflow via interface web e API REST.

Componentes principais:
    - InflowListView: View para listar entradas de produtos (Inflows) com paginação e filtro.
    - InflowCreateView: View para criar novas entradas de produtos.
    - InflowDetailView: View para exibir detalhes de uma entrada específica.
    - InflowCreateListAPIView: API view para listar e criar entradas de produtos.
    - InflowRetrieveAPIView: API view para recuperar detalhes de uma entrada específica.

Dependências:
    - rest_framework.generics: Para as views de API (ListCreateAPIView, RetrieveAPIView).
    - django.contrib.auth.mixins: Para controle de autenticação e permissões (LoginRequiredMixin, PermissionRequiredMixin).
    - django.views.generic: Para as views baseadas em classes (ListView, CreateView, DetailView).
    - django.urls: Para redirecionamento de URLs (reverse_lazy).
    - .models: Para o modelo Inflow.
    - .forms: Para o formulário de criação de Inflow.
    - .serializers: Para a serialização do modelo Inflow na API.
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


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar entradas de produtos (Inflows).

    Esta view exibe uma lista paginada de entradas de produtos, com suporte para filtragem
    por título do produto. Requer autenticação e permissão para visualizar entradas.

    Atributos:
        model (Model): Modelo associado à view (Inflow).
        template_name (str): Nome do template usado para renderizar a lista.
        context_object_name (str): Nome do objeto de contexto no template.
        paginate_by (int): Número de itens por página.
        permission_required (str): Permissão necessária para acessar a view.

    Métodos:
        get_queryset: Filtra a lista de entradas com base no título do produto, se fornecido.
    """

    model = models.Inflow
    template_name = "inflow_list.html"
    context_object_name = "inflows"
    paginate_by = 10
    permission_required = "inflows.view_inflow"

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar novas entradas de produtos (Inflows).

    Esta view exibe um formulário para criar uma nova entrada de produto e redireciona
    para a lista de entradas após a criação. Requer autenticação e permissão para adicionar entradas.

    Atributos:
        model (Model): Modelo associado à view (Inflow).
        template_name (str): Nome do template usado para renderizar o formulário.
        form_class (Form): Classe do formulário usado para criação.
        success_url (str): URL para redirecionamento após a criação.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Inflow
    template_name = "inflow_create.html"
    form_class = forms.InflowForm
    success_url = reverse_lazy("inflow_list")
    permission_required = "inflows.add_inflow"


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View para exibir detalhes de uma entrada de produto (Inflow).

    Esta view exibe os detalhes de uma entrada de produto específica. Requer autenticação
    e permissão para visualizar entradas.

    Atributos:
        model (Model): Modelo associado à view (Inflow).
        template_name (str): Nome do template usado para renderizar os detalhes.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Inflow
    template_name = "inflow_detail.html"
    permission_required = "inflows.view_inflow"


class InflowCreateListAPIView(generics.ListCreateAPIView):
    """
    API View para listar e criar entradas de produtos (Inflows).

    Esta view permite listar todas as entradas de produtos e criar novas entradas
    via API REST.

    Atributos:
        queryset (QuerySet): Conjunto de dados usado para listar entradas.
        serializer_class (Serializer): Classe de serialização para o modelo Inflow.
    """

    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer


class InflowRetrieveAPIView(generics.RetrieveAPIView):
    """
    API View para recuperar detalhes de uma entrada de produto (Inflow).

    Esta view permite recuperar os detalhes de uma entrada de produto específica
    via API REST.

    Atributos:
        queryset (QuerySet): Conjunto de dados usado para recuperar a entrada.
        serializer_class (Serializer): Classe de serialização para o modelo Inflow.
    """

    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer
