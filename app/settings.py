#!/usr/bin/env python
"""Configuração de settings para o projeto Django.

Este módulo contém as configurações principais do projeto Django.

Componentes principais:
    - BASE_DIR: Diretório base do projeto.
    - INSTALLED_APPS: Lista de aplicativos instalados.
    - MIDDLEWARE: Lista de middlewares para processamento de requisições.
    - DATABASES: Configuração do banco de dados.
    - AUTH_PASSWORD_VALIDATORS: Validações de senha.
    - LANGUAGE_CODE e TIME_ZONE: Configurações de internacionalização.
    - STATIC_URL: Caminho para arquivos estáticos.
    - DEFAULT_AUTO_FIELD: Tipo padrão de chave primária.

Fluxo da aplicação:
    1. Define os diretórios e configurações gerais.
    2. Configura o banco de dados e as validações de senha.
    3. Ajusta a internacionalização e arquivos estáticos.
    4. Define configurações para templates e middlewares.

Avisos de segurança:
    - Não exponha `SECRET_KEY` em repositórios públicos.
    - Desative `DEBUG` em ambientes de produção.
    - Defina `ALLOWED_HOSTS` corretamente em produção.

Referências:
    - Documentação oficial:
        https://docs.djangoproject.com/en/5.1/topics/settings/
        https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# ======== Diretórios e Configurações Gerais ======== #
BASE_DIR = Path(__file__).resolve().parent.parent

# ======== Segurança ======== #
SECRET_KEY = "django-insecure-ih93rgg59pd)sptkta-n39mo_hu7fi3$vjo612)vjyod=f-44("
DEBUG = True
ALLOWED_HOSTS = []

# ======== Aplicativos Instalados ======== #
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "authentication",
    "brands",
    "categories",
    "suppliers",
    "products",
    "inflows",
    "outflows",
    "rest_framework",
    "rest_framework_simplejwt",
]

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/login/"

# ======== Middlewares ======== #
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======== Configuração de URLs e WSGI ======== #
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

# ======== Configuração de Templates ======== #
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["app/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ======== Banco de Dados ======== #
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "sge",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "sge_db",
        "PORT": "5432",
    },
    "dev": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

# ======== Validações de Senha ======== #
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ======== Internacionalização ======== #
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ======== Arquivos Estáticos ======== #
STATIC_URL = "static/"

# ======== Configuração Padrão de Chaves Primárias ======== #
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.DjangoModelPermissions",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}
