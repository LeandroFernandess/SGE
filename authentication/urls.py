"""
Módulo de URLs para autenticação com JWT (JSON Web Tokens).

Este módulo define as URLs para obter, atualizar e verificar tokens JWT, que são usados
para autenticação em APIs REST.

Componentes principais:
    - token_obtain_pair: URL para obter um par de tokens (access e refresh).
    - token_refresh: URL para atualizar um token de acesso (access token) usando um token de atualização (refresh token).
    - token_verify: URL para verificar a validade de um token.

Dependências:
    - django.urls.path: Para definir os padrões de URL.
    - rest_framework_simplejwt.views: Para as views de autenticação JWT (TokenObtainPairView, TokenRefreshView, TokenVerifyView).
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(
        "authentication/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "authentication/token/refresh",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "authentication/token/verify",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
]
