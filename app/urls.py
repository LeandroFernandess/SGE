#!/usr/bin/env python
"""
Módulo de configuração de URLs para o projeto Django.

Este módulo define as rotas principais da aplicação Django, mapeando URLs para suas respectivas views.
Ele centraliza as URLs do projeto, incluindo rotas para a administração, autenticação, APIs e apps específicos.

Componentes principais:
    - urlpatterns: Lista que contém as rotas da aplicação.
    - path: Função para mapear URLs para views.
    - include: Função para incluir URLs de outros módulos (apps).

Fluxo da aplicação:
    1. Define a rota para a página de administração do Django (`/admin/`).
    2. Configura rotas para autenticação (login e logout).
    3. Inclui URLs de apps específicos (brands, categories, suppliers, inflows, outflows, products).
    4. Define a rota padrão (home) para a página inicial.

Exemplos:
    - Function-based views:
        path('', views.home, name='home')
    - Class-based views:
        path('login/', auth_views.LoginView.as_view(), name='login')
    - Inclusão de outros URLconfs:
        path('api/v1/', include('authentication.urls'))

Referências:
    - Documentação oficial: https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# Lista de rotas da aplicação
urlpatterns = [
    # Rota para a administração do Django
    path("admin/", admin.site.urls),
    # Rotas para autenticação (login e logout)
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # Rota para a API de autenticação
    path("api/v1/", include("authentication.urls")),
    # Rota padrão para a página inicial
    path("", views.home, name="home"),
    # Inclusão das URLs dos apps específicos
    path("", include("brands.urls")),
    path("", include("categories.urls")),
    path("", include("suppliers.urls")),
    path("", include("inflows.urls")),
    path("", include("outflows.urls")),
    path("", include("products.urls")),
]
