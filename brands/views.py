"""
Módulo de views para o modelo Brand.

Este módulo define as views baseadas em classes para listar, criar, detalhar, atualizar, excluir
e interagir com o modelo Brand via interface web e API REST.

Componentes principais:
    - BrandListView: View para listar marcas com paginação e filtro.
    - BrandCreateView: View para criar novas marcas.
    - BrandDetailView: View para exibir detalhes de uma marca específica.
    - BrandUpdateView: View para atualizar uma marca específica.
    - BrandDeleteView: View para excluir uma marca específica.
    - BrandCreateListAPIView: API view para listar e criar marcas.
    - BrandRetrieveUpdateDestroyAPIView: API view para recuperar, atualizar e excluir uma marca.

Dependências:
    - rest_framework.generics: Para as views de API (ListCreateAPIView, RetrieveUpdateDestroyAPIView).
    - django.contrib.auth.mixins: Para controle de autenticação e permissões (LoginRequiredMixin, PermissionRequiredMixin).
    - django.views.generic: Para as views baseadas em classes (ListView, CreateView, DetailView, UpdateView, DeleteView).
    - django.urls: Para redirecionamento de URLs (reverse_lazy).
    - .models: Para o modelo Brand.
    - .forms: Para o formulário de criação e atualização de Brand.
    - .serializers: Para a serialização do modelo Brand na API.
"""

from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from . import models, forms, serializers


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar marcas.

    Esta view exibe uma lista paginada de marcas, com suporte para filtragem
    por nome. Requer autenticação e permissão para visualizar marcas.

    Atributos:
        model (Model): Modelo associado à view (Brand).
        template_name (str): Nome do template usado para renderizar a lista.
        context_object_name (str): Nome do objeto de contexto no template.
        paginate_by (int): Número de itens por página.
        permission_required (str): Permissão necessária para acessar a view.

    Métodos:
        get_queryset: Filtra a lista de marcas com base no nome, se fornecido.
    """

    model = models.Brand
    template_name = "brand_list.html"
    context_object_name = "brands"
    paginate_by = 10
    permission_required = "brands.view_brand"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar novas marcas.

    Esta view exibe um formulário para criar uma nova marca e redireciona
    para a lista de marcas após a criação. Requer autenticação e permissão para adicionar marcas.

    Atributos:
        model (Model): Modelo associado à view (Brand).
        template_name (str): Nome do template usado para renderizar o formulário.
        form_class (Form): Classe do formulário usado para criação.
        success_url (str): URL para redirecionamento após a criação.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Brand
    template_name = "brand_create.html"
    form_class = forms.BrandForm
    success_url = reverse_lazy("brand_list")
    permission_required = "brands.add_brand"


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View para exibir detalhes de uma marca.

    Esta view exibe os detalhes de uma marca específica. Requer autenticação
    e permissão para visualizar marcas.

    Atributos:
        model (Model): Modelo associado à view (Brand).
        template_name (str): Nome do template usado para renderizar os detalhes.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Brand
    template_name = "brand_detail.html"
    permission_required = "brands.view_brand"


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    View para atualizar uma marca.

    Esta view exibe um formulário para atualizar uma marca existente e redireciona
    para a lista de marcas após a atualização. Requer autenticação e permissão para alterar marcas.

    Atributos:
        model (Model): Modelo associado à view (Brand).
        template_name (str): Nome do template usado para renderizar o formulário.
        form_class (Form): Classe do formulário usado para atualização.
        success_url (str): URL para redirecionamento após a atualização.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Brand
    template_name = "brand_update.html"
    form_class = forms.BrandForm
    success_url = reverse_lazy("brand_list")
    permission_required = "brands.change_brand"


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    View para excluir uma marca.

    Esta view exibe uma confirmação para excluir uma marca e redireciona
    para a lista de marcas após a exclusão. Requer autenticação e permissão para excluir marcas.

    Atributos:
        model (Model): Modelo associado à view (Brand).
        template_name (str): Nome do template usado para renderizar a confirmação.
        success_url (str): URL para redirecionamento após a exclusão.
        context_object_name (str): Nome do objeto de contexto no template.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Brand
    template_name = "brand_delete.html"
    success_url = reverse_lazy("brand_list")
    context_object_name = "brand"
    permission_required = "brands.delete_brand"


class BrandCreateListAPIView(generics.ListCreateAPIView):
    """
    API View para listar e criar marcas.

    Esta view permite listar todas as marcas e criar novas marcas
    via API REST.

    Atributos:
        queryset (QuerySet): Conjunto de dados usado para listar marcas.
        serializer_class (Serializer): Classe de serialização para o modelo Brand.
    """

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View para recuperar, atualizar e excluir uma marca.

    Esta view permite recuperar, atualizar e excluir os detalhes de uma marca específica
    via API REST.

    Atributos:
        queryset (QuerySet): Conjunto de dados usado para recuperar a marca.
        serializer_class (Serializer): Classe de serialização para o modelo Brand.
    """

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
