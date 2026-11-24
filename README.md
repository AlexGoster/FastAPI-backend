# FastAPI Backend

Регистрация, access JWT и CRUD собственных Items на FastAPI/SQLAlchemy.
Refresh-токены, роли администратора и rate limiting не реализованы.

[Проверенный запуск и ограничения](VERIFICATION.md).

```bash
python -m venv .venv
# Активируйте .venv согласно ОС.
python -m pip install -r requirements.txt
```

Создайте исключённый из Git локальный `.env`:

```dotenv
DATABASE_URL=sqlite+aiosqlite:///./app.db
SECRET_KEY=local-test-key-change-before-any-public-use
```

Для PostgreSQL URL имеет вид `postgresql+asyncpg://user:password@localhost/test_database`.

```bash
python -m alembic upgrade head
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Swagger `/docs`, health `/health`. POST `/auth/register` принимает JSON email/password,
POST `/auth/login` — форму username/password; GET `/auth/me` и `/users/me` — профиль.
GET/POST `/items/`, GET/PATCH/DELETE `/items/{id}` требуют Bearer access token.
Список содержит только свои Items; чужой ID возвращает 404.

```bash
docker compose -p backend-local up -d --build
docker compose -p backend-local exec app python -m alembic upgrade head
python -m pytest -o addopts= -q
```

SQLite-тесты и Docker HTTP на отдельном PostgreSQL прошли.
Пароли в Compose предназначены только для локального стенда.
