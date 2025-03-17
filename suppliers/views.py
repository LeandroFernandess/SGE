"""
Módulo de views para gerenciamento de fornecedores.

Este módulo contém classes de views para listar, criar, detalhar, atualizar e excluir fornecedores,
tanto para interfaces web quanto para APIs REST. As views web requerem autenticação e permissões específicas.

Componentes principais:
    - SupplierListView: Lista fornecedores com paginação e filtragem.
    - SupplierCreateView: Cria um novo fornecedor.
    - SupplierDetailView: Exibe detalhes de um fornecedor.
    - SupplierUpdateView: Atualiza um fornecedor existente.
    - SupplierDeleteView: Exclui um fornecedor.
    - SupplierCreateListAPIView: API para listar e criar fornecedores.
    - SupplierRetrieveUpdateDestroyAPIView: API para recuperar, atualizar e excluir fornecedores.

Fluxo típico:
    1. O usuário acessa a lista de fornecedores.
    2. O usuário pode criar um novo fornecedor ou visualizar detalhes de um existente.
    3. O usuário pode atualizar ou excluir um fornecedor, se tiver permissões.
    4. As APIs REST permitem operações similares via endpoints.

Dependências:
    - django.contrib.auth.mixins: Para autenticação e permissões.
    - rest_framework.generics: Para views de API.
    - .models: Modelos de dados, incluindo Supplier.
    - .forms: Formulários, incluindo SupplierForm.
    - .serializers: Serializadores para API, incluindo SupplierSerializer.
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


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    View para listar fornecedores com paginação e filtragem.

    Esta view exibe uma lista paginada de fornecedores e permite filtrar por nome.
    Requer autenticação e a permissão 'suppliers.view_supplier'.

    Atributos:
        model: Modelo Supplier.
        template_name: Template HTML para renderizar a lista.
        context_object_name: Nome do objeto no contexto do template.
        paginate_by: Número de itens por página.
        permission_required: Permissão necessária para acessar a view.

    Métodos sobrescritos:
        get_queryset: Filtra o queryset baseado no parâmetro 'name' da query string.
    """

    model = models.Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"
    paginate_by = 5
    permission_required = "suppliers.view_supplier"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View para criar um novo fornecedor.

    Esta view apresenta um formulário para criar um novo fornecedor e redireciona para a lista
    de fornecedores após o sucesso. Requer autenticação e a permissão 'suppliers.view_supplier'.

    Atributos:
        model: Modelo Supplier.
        template_name: Template HTML para renderizar o formulário.
        form_class: Formulário usado para criar o fornecedor.
        success_url: URL para redirecionar após a criação.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Supplier
    template_name = "supplier_create.html"
    form_class = forms.SupplierForm
    success_url = reverse_lazy("supplier_list")
    permission_required = "suppliers.view_supplier"


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View para exibir detalhes de um fornecedor.

    Esta view exibe informações detalhadas de um fornecedor específico.
    Requer autenticação e a permissão 'suppliers.view_supplier'.

    Atributos:
        model: Modelo Supplier.
        template_name: Template HTML para renderizar os detalhes.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Supplier
    template_name = "supplier_detail.html"
    permission_required = "suppliers.view_supplier"


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    View para atualizar um fornecedor existente.

    Esta view apresenta um formulário para editar um fornecedor e redireciona para a lista
    de fornecedores após o sucesso. Requer autenticação e a permissão 'suppliers.view_supplier'.

    Atributos:
        model: Modelo Supplier.
        template_name: Template HTML para renderizar o formulário.
        form_class: Formulário usado para atualizar o fornecedor.
        success_url: URL para redirecionar após a atualização.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Supplier
    template_name = "supplier_update.html"
    form_class = forms.SupplierForm
    success_url = reverse_lazy("supplier_list")
    permission_required = "suppliers.view_supplier"


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    View para excluir um fornecedor.

    Esta view confirma a exclusão de um fornecedor e redireciona para a lista de fornecedores.
    Requer autenticação e a permissão 'suppliers.view_supplier'.

    Atributos:
        model: Modelo Supplier.
        template_name: Template HTML para confirmar a exclusão.
        success_url: URL para redirecionar após a exclusão.
        context_object_name: Nome do objeto no contexto do template.
        permission_required: Permissão necessária para acessar a view.
    """

    model = models.Supplier
    template_name = "supplier_delete.html"
    success_url = reverse_lazy("supplier_list")
    context_object_name = "supplier"
    permission_required = "suppliers.view_supplier"


class SupplierCreateListAPIView(generics.ListCreateAPIView):
    """
    API view para listar e criar fornecedores.

    Esta view permite listar todos os fornecedores ou criar um novo via métodos GET e POST.
    Usa o serializer SupplierSerializer para serializar os dados.

    Atributos:
        queryset: Todos os objetos Supplier.
        serializer_class: Serializer para Supplier.
    """

    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view para recuperar, atualizar e excluir um fornecedor.

    Esta view permite recuperar, atualizar ou excluir um fornecedor específico via métodos GET, PUT, PATCH e DELETE.
    Usa o serializer SupplierSerializer para serializar os dados.

    Atributos:
        queryset: Todos os objetos Supplier.
        serializer_class: Serializer para Supplier.
    """

    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
