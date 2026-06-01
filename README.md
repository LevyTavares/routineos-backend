# 🚀 RoutineOS Backend

Backend da plataforma RoutineOS.

Sistema de produtividade pessoal focado em hábitos, tarefas, estudos e gerenciamento de foco.

## Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib + bcrypt
- JWT Authentication

## Features atuais

✅ FastAPI API

✅ SQLite Database

✅ User CRUD

✅ Password Hashing

✅ Swagger Docs

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

## Instalação

Clone:

```bash
git clone https://github.com/LevyTavares/routineos-backend.git
```

Entrar:

```bash
cd routineos-backend
```

Criar venv:

```bash
python -m venv venv
```

Ativar:

Linux/macOS:

```bash
source venv/bin/activate
```

Instalar:

```bash
pip install -r requirements.txt
```

Executar:

```bash
uvicorn app.main:app --reload
```

Swagger:

```txt
http://127.0.0.1:8000/docs
```

## Próximas features

- JWT Login
- Protected Routes
- Habits CRUD
- Tasks CRUD
- Analytics