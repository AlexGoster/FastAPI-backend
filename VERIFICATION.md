# Проверка проекта

Проверки выполнялись 10–20 октября 2026. Исходная рабочая копия была чистой.

6 тестов прошли. JWT/register/login/me, собственные Items CRUD, запрет доступа к чужим Items; SQLite-тесты и Alembic upgrade/downgrade/upgrade.

Нет refresh-токенов, ролей администратора и включённого rate limiting.

## Повторный запуск

Команды из папки проекта после создания и активации Python venv. Для API задайте DATABASE_URL отдельной локальной БД и тестовый SECRET_KEY по примеру конфигурации; не используйте рабочие подключения.

```bash
python -m venv .venv
# Активируйте .venv согласно ОС.
python -m pip install -r requirements.txt
python -m alembic upgrade head
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Тесты в отдельном тестовом окружении:

```bash
python -m pytest -o addopts= -q
```

Docker-проверки использовали отдельную сеть, PostgreSQL *_test и Redis; реальные данные, платежи и внешние сообщения не затрагивались. Результат локального запуска не означает production-ready.

Docker build и реальный HTTP CRUD с PostgreSQL прошли 20 октября.
