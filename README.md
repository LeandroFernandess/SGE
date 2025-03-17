# Sistema de Gerenciamento de Estoque (SGE)🚀

Um sistema desenvolvido com Django, HTML, CSS e JavaScript para gerenciamento de marcas, categorias e métricas. O projeto permite criar, editar, visualizar e excluir registros, além de contar com autenticação de usuários.

## Tecnologias Utilizadas 🛠️

- **Django**: Framework principal para o backend.
- **Python**: Linguagem de programação utilizada.
- **HTML/CSS**: Para estruturação e estilização das páginas.
- **JavaScript**: Para funcionalidades interativas.
- **PostgreSQL/SQLite**: Banco de dados para armazenamento de informações.

## Estrutura do Projeto 📂

```
SGE/
├── app/
│   ├── templates/
│   │   ├── components/
│   │   │   ├── _footer.html
│   │   │   ├── _header.html
│   │   │   ├── _pagination.html
│   │   │   ├── _product_metrics.html
│   │   │   ├── _sales_metrics.html
│   │   │   ├── _sidebar.html
│   │   ├── registration/
│   │   │   ├── login.html
│   │   ├── base.html
│   │   ├── home.html
│   ├── asgi.py
│   ├── settings.py
│   ├── metrics.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│
├── authentication/
│   ├── migrations/
│   ├── apps.py
│   ├── urls.py
│
├── brands/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   ├── templates/
│   │   ├── brand_create.html
│   │   ├── brand_delete.html
│   │   ├── brand_detail.html
│   │   ├── brand_list.html
│   │   ├── brand_update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── categories/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   ├── templates/
│   │   ├── category_create.html
│   │   ├── category_delete.html
│   │   ├── category_detail.html
│   │   ├── category_list.html
│   │   ├── category_update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── inflows/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   ├── templates/
│   │   ├── inflow_create.html
│   │   ├── inflow_delete.html
│   │   ├── inflow_detail.html
│   │   ├── inflow_list.html
│   │   ├── inflow_update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── views.py
│   ├── urls.py
│
├── outflows/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   ├── templates/
│   │   ├── outflow_create.html
│   │   ├── outflow_delete.html
│   │   ├── outflow_detail.html
│   │   ├── outflow_list.html
│   │   ├── outflow_update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── views.py
│   ├── urls.py
│
├── products/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   ├── templates/
│   │   ├── product_create.html
│   │   ├── product_delete.html
│   │   ├── product_detail.html
│   │   ├── product_list.html
│   │   ├── product_update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── suppliers/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   ├── templates/
│   │   ├── supplier_create.html
│   │   ├── supplier_delete.html
│   │   ├── supplier_detail.html
│   │   ├── supplier_list.html
│   │   ├── supplier_update.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── .flake8
├── .gitignore
├── manage.py
├── requirements_dev.txt
├── requirements.txt
```

## Principais Pastas e Arquivos

- **app/**: Contém as configurações do projeto e templates compartilhados.
- **authentication/**: Gerencia autenticação de usuários.
- **brands/**: CRUD completo para gerenciamento de marcas.
- **categories/**: CRUD para gerenciamento de categorias.
- **templates/**: Páginas HTML organizadas por componentes e módulos.

## Funcionalidades 🚀

✅ Autenticação de usuários.
✅ CRUD completo para marcas e categorias.
✅ Métricas detalhadas de produtos e vendas.
✅ Interface amigável com componentes reutilizáveis.

## Como Executar o Projeto 🔧

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/django-project.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd django-project
   ```
3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Mac/Linux
   source venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
7. Acesse o projeto no navegador:
   ```
   http://127.0.0.1:8000/
   ```

## Contribuindo 🤝

Contribuições são bem-vindas! Caso tenha sugestões ou encontre problemas, abra uma issue ou envie um pull request.

## Contato 💬

📧 Email: leandrofernandes1600@gmail.com  
🐙 GitHub: [LeandroFernandess](https://github.com/LeandroFernandess)

