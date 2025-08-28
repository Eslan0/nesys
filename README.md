# Nesys

## Routes

| Method | Route/Endpoint       | Description                    | Parameters      | Authentication |
|--------|----------------------|--------------------------------|-----------------|----------------|
| GET    | `/`                  | Home (inicio).                 | None            | No             |
| GET    | `/login`             | Panel de login.                | None            | No             |
| GET    | `/signup`            | Panel de cadrastro.            | None            | No             |
| POST   | `/login`             | Enviar formulario de login.    | User data       | No             |
| POST   | `/signup`            | Enviar formulario de cadrastro.| User data       | No             |
| GET    | `/users`             | Lista todos os usuários.       | None            | Yes            |
| POST   | `/users`             | Cria um novo usuário.          | User data       | Yes            |
| GET    | `/users/{id}`        | Retorna um usuário específico. | `id` (in URL)   | Yes            |
| PUT    | `/users/{id}`        | Atualiza um usuário existente. | `id` (in URL), User data | Yes   |
| DELETE | `/users/{id}`        | Exclui um usuário.             | `id` (in URL)   | Yes            |
| GET    | `/products`          | Retorna a lista de produtos.   | `limit`, `offset` | No           |
| GET    | `/products/{id}`     | Retorna um produto específico. | `id` (in URL)   | No             |
| GET    | `/orders`            | Rertonar lista de pedidos.     | None            | Yes            |
| GET    | `/orders/{id}`       | Rertonar um pedido específico. | `id` (in URL)   | Yes            |
| POST   | `/orders/{id}`       | Cria um novo pedido.           | Order data      | Yes            |
| PUT    | `/orders/{id}`       | Atualizar um pedido.           | `id` (in URL), Order data | Yes  |
| DELETE | `/orders/{id}`       | Exclui um pedido.              | `id` (in URL)   | Yes            |

---

### Project Structure

```bach
ecommerce/
├── .venv/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── home_routes.py
│   │   ├── order_routes.py
│   │   ├── product_routes.py
│   │   └── user_routes.py
│   ├── services/
│   │   ├── user_service.py
│   │   └── product_service.py
│   ├── static/
│   ├── templates/
│   │   ├── auth/
│   │   ├── home/
│   │   ├── orders/
│   │   ├── products/
│   │   └── users/
│   ├── utils/
│   │   └── helpers.py
│   └── __init__.py
├── migrations/
├── tests/
│   ├── test_users.py
│   └── test_products.py
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```
