# 🚀 RoutineOS Backend

Backend da plataforma RoutineOS — sistema de produtividade pessoal para gerenciamento de hábitos, tarefas, estudos e foco.

## Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib + bcrypt
- Python-Jose (JWT)

## Features atuais

✅ User CRUD

✅ Password Hashing

✅ SQLite Database

✅ FastAPI Swagger Docs

## Estrutura

```txt
app/
├── routers/
├── models/
├── schemas/
├── services/
├── database.py
└── main.py
```

## Rodando localmente

Criar ambiente:

```bash
python -m venv venv
```

Ativar:

Linux/macOS:

```bash
source venv/bin/activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Rodar API:

```bash
uvicorn app.main:app --reload
```

Swagger:

http://127.0.0.1:8000/docs