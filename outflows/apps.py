from django.apps import AppConfig

"""
Módulo de configuração da aplicação Outflows.

Este módulo define a configuração da aplicação 'outflows' no Django,
especificando o tipo de campo automático padrão e carregando sinais associados.

Componentes principais:
    - OutflowsConfig: Classe de configuração da aplicação Outflows.

Dependências:
    - django.apps: Para a criação de configurações de aplicações.
"""


class OutflowsConfig(AppConfig):
    """
    Classe de configuração para a aplicação Outflows.

    Define as configurações da aplicação 'outflows', como o tipo de campo automático
    para chaves primárias e o carregamento de sinais ao iniciar a aplicação.

    Atributos:
        default_auto_field: Tipo de campo automático padrão para chaves primárias (BigAutoField).
        name: Nome da aplicação no projeto Django ("outflows").

    Métodos:
        ready: Carrega os sinais definidos no módulo outflows.signals ao iniciar a aplicação.

    Exemplo de uso:
        Esta classe é automaticamente carregada pelo Django quando a aplicação 'outflows'
        é incluída em INSTALLED_APPS no settings.py.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "outflows"

    def ready(self):
        """
        Método chamado quando a aplicação está pronta.

        Importa o módulo outflows.signals para registrar os sinais associados à aplicação,
        garantindo que eles sejam carregados durante a inicialização.

        Nota:
            O uso de # noqa: F401 ignora avisos de linting sobre importação não utilizada.
        """
        import outflows.signals  # noqa: F401
