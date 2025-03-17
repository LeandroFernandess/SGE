"""
Módulo de views para o modelo Category.

Este módulo define as views baseadas em classes para listar, criar, detalhar, atualizar, excluir
e interagir com o modelo Category via interface web e API REST.

Componentes principais:
    - CategoryListView: View para listar categorias com paginação e filtro.
    - CategoryCreateView: View para criar novas categorias.
    - CategoryDetailView: View para exibir detalhes de uma categoria específica.
    - CategoryUpdateView: View para atualizar uma categoria específica.
    - CategoryDeleteView: View para excluir uma categoria específica.
    - CategoryCreateListAPIView: API view para listar e criar categorias.
    - CategoryRetrieveUpdateDestroyAPIView: API view para recuperar, atualizar e excluir uma categoria.

Dependências:
    - rest_framework.generics: Para as views de API (ListCreateAPIView, RetrieveUpdateDestroyAPIView).
    - django.contrib.auth.mixins: Para controle de autenticação e permissões (LoginRequiredMixin, PermissionRequiredMixin).
    - django.views.generic: Para as views baseadas em classes (ListView, CreateView, DetailView, UpdateView, DeleteView).
    - django.urls: Para redirecionamento de URLs (reverse_lazy).
    - .models: Para o modelo Category.
    - .forms: Para o formulário de criação e atualização de Category.
    - .serializers: Para a serialização do modelo Category na API.
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


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar categorias.

    Esta view exibe uma lista paginada de categorias, com suporte para filtragem
    por nome. Requer autenticação e permissão para visualizar categorias.

    Atributos:
        model (Model): Modelo associado à view (Category).
        template_name (str): Nome do template usado para renderizar a lista.
        context_object_name (str): Nome do objeto de contexto no template.
        paginate_by (int): Número de itens por página.
        permission_required (str): Permissão necessária para acessar a view.

    Métodos:
        get_queryset: Filtra a lista de categorias com base no nome, se fornecido.
    """

    model = models.Category
    template_name = "category_list.html"
    context_object_name = "categories"
    paginate_by = 5
    permission_required = "categories.view_category"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar novas categorias.

    Esta view exibe um formulário para criar uma nova categoria e redireciona
    para a lista de categorias após a criação. Requer autenticação e permissão para adicionar categorias.

    Atributos:
        model (Model): Modelo associado à view (Category).
        template_name (str): Nome do template usado para renderizar o formulário.
        form_class (Form): Classe do formulário usado para criação.
        success_url (str): URL para redirecionamento após a criação.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Category
    template_name = "category_create.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category_list")
    permission_required = "categories.add_category"


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View para exibir detalhes de uma categoria.

    Esta view exibe os detalhes de uma categoria específica. Requer autenticação
    e permissão para visualizar categorias.

    Atributos:
        model (Model): Modelo associado à view (Category).
        template_name (str): Nome do template usado para renderizar os detalhes.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Category
    template_name = "category_detail.html"
    permission_required = "categories.view_category"


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    View para atualizar uma categoria.

    Esta view exibe um formulário para atualizar uma categoria existente e redireciona
    para a lista de categorias após a atualização. Requer autenticação e permissão para alterar categorias.

    Atributos:
        model (Model): Modelo associado à view (Category).
        template_name (str): Nome do template usado para renderizar o formulário.
        form_class (Form): Classe do formulário usado para atualização.
        success_url (str): URL para redirecionamento após a atualização.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Category
    template_name = "category_update.html"
    form_class = forms.CategoryForm
    success_url = reverse_lazy("category_list")
    permission_required = "categories.change_category"


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    View para excluir uma categoria.

    Esta view exibe uma confirmação para excluir uma categoria e redireciona
    para a lista de categorias após a exclusão. Requer autenticação e permissão para excluir categorias.

    Atributos:
        model (Model): Modelo associado à view (Category).
        template_name (str): Nome do template usado para renderizar a confirmação.
        success_url (str): URL para redirecionamento após a exclusão.
        context_object_name (str): Nome do objeto de contexto no template.
        permission_required (str): Permissão necessária para acessar a view.
    """

    model = models.Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("category_list")
    context_object_name = "category"
    permission_required = "categories.delete_category"


class CategoryCreateListAPIView(generics.ListCreateAPIView):
    """
    API View para listar e criar categorias.

    Esta view permite listar todas as categorias e criar novas categorias
    via API REST.

    Atributos:
        queryset (QuerySet): Conjunto de dados usado para listar categorias.
        serializer_class (Serializer): Classe de serialização para o modelo Category.
    """

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View para recuperar, atualizar e excluir uma categoria.

    Esta view permite recuperar, atualizar e excluir os detalhes de uma categoria específica
    via API REST.

    Atributos:
        queryset (QuerySet): Conjunto de dados usado para recuperar a categoria.
        serializer_class (Serializer): Classe de serialização para o modelo Category.
    """

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
