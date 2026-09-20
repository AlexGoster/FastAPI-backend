# FastAPI Backend

REST API с авторизацией, CRUD операциями и PostgreSQL.

## Возможности

- JWT аутентификация
- CRUD операции для Users и Items
- Rate Limiting
- Alembic миграции
- Docker деплой
- Автоматические тесты

## Установка

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Docker

```bash
docker-compose up -d
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Регистрация |
| POST | /login | Вход |
| GET | /users/me | Профиль |
| GET | /items | Список items |
| POST | /items | Создать item |

MIT License - AlexGoster
