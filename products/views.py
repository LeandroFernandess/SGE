"""
Módulo de views para gerenciamento de produtos.

Este módulo contém classes de views para listar, criar, detalhar, atualizar e excluir produtos,
tanto para interfaces web quanto para APIs REST. As views web exigem autenticação e permissões específicas,
enquanto as views de API fornecem endpoints para operações CRUD.

Componentes principais:
    - ProductListView: Lista produtos com filtros e métricas adicionais.
    - ProductCreateView: Cria um novo produto.
    - ProductDetailView: Exibe detalhes de um produto.
    - ProductUpdateView: Atualiza um produto existente.
    - ProductDeleteView: Exclui um produto.
    - ProductCreateListAPIView: API para listar e criar produtos.
    - ProductRetrieveUpdateDestroyAPIView: API para recuperar, atualizar e excluir produtos.

Fluxo típico:
    1. O usuário acessa a lista de produtos com filtros opcionais.
    2. O usuário pode criar, visualizar, atualizar ou excluir produtos, conforme permissões.
    3. As APIs REST permitem operações equivalentes via endpoints.

Dependências:
    - django.contrib.auth.mixins: Para autenticação e permissões.
    - rest_framework.generics: Para views de API.
    - .models, .forms, .serializers: Modelos, formulários e serializadores locais.
    - categories.models, brands.models: Modelos relacionados de categorias e marcas.
    - app.metrics: Funções para métricas de produtos.
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
from categories.models import Category
from brands.models import Brand
from app import metrics


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar produtos com paginação e filtragem.

    Exibe uma lista paginada de produtos com filtros por título, número de série, categoria e marca.
    Requer autenticação e a permissão 'products.view_product'. Inclui métricas e dados adicionais no contexto.

    Atributos:
        model: Modelo Product.
        template_name: Template HTML para renderizar a lista.
        context_object_name: Nome do objeto no contexto do template.
        paginate_by: Número de itens por página.
        permission_required: Permissão necessária para acessar a view.

    Métodos sobrescritos:
        get_queryset: Filtra o queryset com base nos parâmetros da query string.
        get_context_data: Adiciona métricas, categorias e marcas ao contexto do template.
    """

    model = models.Product
    template_name = "product_list.html"
    context_object_name = "products"
    paginate_by = 5
    permission_required = "products.view_product"

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")
        serie_number = self.request.GET.get("serie_number")
        category = self.request.GET.get("category")
        brand = self.request.GET.get("brand")
        if title:
            queryset = queryset.filter(title__icontains=title)
        if category:
            queryset = queryset.filter(category__name=category)
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
        if brand:
            queryset = queryset.filter(brand__name=brand)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_metrics"] = metrics.get_product_metrics()
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar um novo produto.

    Apresenta um formulário para criar um produto e redireciona para a lista de produtos após o sucesso.
    Requer autenticação e a permissão 'products.add_product'.

    Atributos:
        model: Modelo Product.
        template_name: Template HTML para renderizar o formulário.
        form_class: Formulário usado para criar o produto.
        success_url: URL para redirecionar após a criação.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Product
    template_name = "product_create.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")
    permission_required = "products.add_product"


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View para exibir detalhes de um produto.

    Exibe informações detalhadas de um produto específico.
    Requer autenticação e a permissão 'products.view_product'.

    Atributos:
        model: Modelo Product.
        template_name: Template HTML para renderizar os detalhes.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Product
    template_name = "product_detail.html"
    permission_required = "products.view_product"


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    View para atualizar um produto existente.

    Apresenta um formulário para editar um produto e redireciona para a lista de produtos após o sucesso.
    Requer autenticação e a permissão 'products.change_product'.

    Atributos:
        model: Modelo Product.
        template_name: Template HTML para renderizar o formulário.
        form_class: Formulário usado para atualizar o produto.
        success_url: URL para redirecionar após a atualização.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Product
    template_name = "product_update.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")
    permission_required = "products.change_product"


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    View para excluir um produto.

    Confirma a exclusão de um produto e redireciona para a lista de produtos.
    Requer autenticação e a permissão 'products.delete_product'.

    Atributos:
        model: Modelo Product.
        template_name: Template HTML para confirmar a exclusão.
        success_url: URL para redirecionar após a exclusão.
        context_object_name: Nome do objeto no contexto do template.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("product_list")
    context_object_name = "product"
    permission_required = "products.delete_product"


class ProductCreateListAPIView(generics.ListCreateAPIView):
    """
    API view para listar e criar produtos.

    Permite listar todos os produtos ou criar um novo via métodos GET e POST.
    Usa o serializer ProductSerializer para serializar os dados.

    Atributos:
        queryset: Todos os objetos Product.
        serializer_class: Serializer para Product.
    """

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view para recuperar, atualizar e excluir um produto.

    Permite recuperar, atualizar ou excluir um produto específico via métodos GET, PUT, PATCH e DELETE.
    Usa o serializer ProductSerializer para serializar os dados.

    Atributos:
        queryset: Todos os objetos Product.
        serializer_class: Serializer para Product.
    """

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
