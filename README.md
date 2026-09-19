# FastAPI Backend

REST API для управления пользователями и задачами с JWT-авторизацией.

## Описание

Бэкенд-приложение на FastAPI с полным циклом: регистрация, авторизация, CRUD-операции, миграции базы данных, Docker-деплой.

## Технологии

- **Язык:** Python 3.11+
- **Фреймворк:** FastAPI, SQLAlchemy, Pydantic
- **База данных:** PostgreSQL, Alembic (миграции)
- **Авторизация:** JWT (access/refresh токены)
- **Деплой:** Docker, docker-compose
- **Тестирование:** pytest, httpx

## Возможности

- Регистрация и вход пользователей (JWT)
- CRUD операции для Users и Items
- Ролевая система (admin/user)
- Rate Limiting (защита от спама)
- Автоматические миграции через Alembic
- Swagger-документация (/docs)
- Health check эндпоинт

## Установка и запуск

```bash
# Клонирование
git clone https://github.com/AlexGoster/FastAPI-backend.git
cd FastAPI-backend

# Установка зависимостей
pip install -r requirements.txt

# Настройка (.env)
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key

# Запуск
uvicorn main:app --reload
```

## Docker

```bash
docker-compose up -d
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | /register | No | Регистрация пользователя |
| POST | /login | No | Получение JWT токена |
| GET | /users/me | Yes | Текущий пользователь |
| GET | /items | Yes | Список items |
| POST | /items | Yes | Создать item |
| PUT | /items/{id} | Yes | Обновить item |
| DELETE | /items/{id} | Yes | Удалить item |

## Структура проекта

```
FastAPI-backend/
├── main.py              # Точка входа
├── config.py            # Конфигурация
├── database.py          # Подключение к БД
├── models/              # SQLAlchemy модели
├── schemas/             # Pydantic схемы
├── auth/                # JWT логика
├── routers/             # API маршруты
├── middleware/          # CORS, Rate Limiting
├── tests/               # Тесты
├── alembic/             # Миграции
├── Dockerfile
└── docker-compose.yml
```

## Что я изучила

- Проектирование REST API на FastAPI
- Работа с SQLAlchemy ORM и Alembic миграциями
- JWT-авторизация и безопасность
- Docker-деплой бэкенд-приложений
- Написание тестов на pytest

## License

MIT License - AlexGoster


Last updated: 2026-09-20


Last updated: 2026-09-20


Last updated: 2026-09-20


Last updated: 2026-09-23


Last updated: 2026-09-23


Last updated: 2026-09-23


Last updated: 2026-09-21


Last updated: 2026-09-21


Last updated: 2026-09-21


Last updated: 2026-09-22


Last updated: 2026-09-22


Last updated: 2026-09-22


Last updated: 2026-09-19


Last updated: 2026-09-19


Last updated: 2026-09-19
