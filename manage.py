#!/usr/bin/env python
"""Utilitário de linha de comando para tarefas administrativas do Django.

Este módulo é o ponto de entrada para executar comandos administrativos do Django, como
iniciar o servidor, criar migrações ou executar testes.

Componentes principais:
    - main: Configura o ambiente Django e executa comandos administrativos.

Fluxo básico:
    1. Define o módulo de configurações do Django.
    2. Importa e executa os comandos fornecidos via linha de comando.
    3. Trata erros de importação, caso o Django não esteja disponível.

Exceções:
    - ImportError: Levantada se o Django não estiver instalado ou acessível.
"""

import os
import sys


def main():
    """Executa tarefas administrativas do Django a partir da linha de comando.

    Configura o ambiente Django e delega a execução de comandos administrativos ao
    módulo `django.core.management`.

    Etapas:
        1. Define a variável de ambiente `DJANGO_SETTINGS_MODULE` como "app.settings".
        2. Tenta importar `execute_from_command_line` de `django.core.management`.
        3. Executa os comandos passados via `sys.argv`.
        4. Se a importação falhar, levanta uma exceção com detalhes sobre o erro.

    Exceções:
        - ImportError: Levantada se o Django não estiver instalado ou se o ambiente
          virtual não estiver ativado.

    Exemplo de uso:
        python manage.py runserver
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
