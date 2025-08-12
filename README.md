# Nesys

``` lua
ecommerce/
│
├── .venv/                     # Ambiente virtual (não versionar)
├── .env                       # Variáveis de ambiente
├── .gitignore
├── requirements.txt           # Dependências do projeto
├── run.py                     # Arquivo para iniciar o app
│
├── config.py                  # Configurações (Dev, Prod, Test)
│
├── app/                       # Pasta principal do app
│   ├── __init__.py            # Criação do app Flask
│   ├── routes.py              # Rotas principais (separar depois)
│   ├── models/                # Modelos do banco de dados
│   │   └── user.py            # Ex: Modelo de Usuário
│   │   └── product.py         # Ex: Modelo de Produto
│   │
│   ├── templates/             # Templates HTML (corrigir nome)
│   ├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   ├── views/                 # Blueprints para páginas (opcional)
│   └── utils/                 # Funções utilitárias
│
└── migrations/                # Arquivos de migração do banco (alembic/flask-migrate)
```
