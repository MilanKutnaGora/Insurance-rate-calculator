# Cargo_insurance Rate Calculator API

Этот проект представляет собой REST API сервис для расчета стоимости страхования в зависимости от типа груза и объявленной стоимости. API разработан с использованием FastAPI, SQLAlchemy ORM и PostgreSQL, и развертывается с помощью Docker и Docker Compose.

## Особенности

- Расчет стоимости страхования на основе типа груза и объявленной стоимости
- CRUD операции для управления тарифами
- Логирование действий через Kafka
- Развертывание в Docker контейнерах

## Требования

- Docker
- Docker Compose

## Установка и запуск

1. Клонируйте репозиторий:

`git clone https://github.com/MilanKutnaGora/Insurance-rate-calculator.git`

`cd insurance-rate-calculator`

2. Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные окружения:

`DATABASE_URL=`

`KAFKA_BOOTSTRAP_SERVERS=`

3. Запустите приложение с помощью Docker Compose:

`docker-compose up --build`

4. API будет доступно по адресу
`http://localhost:8000`. 
5. Документация Swagger UI доступна по адресу 
`http://localhost:8000/docs`.

## Использование API

### Расчет стоимости страхования

POST `/calculate_insurance`

Пример запроса:
```json
{
"date": "2020-06-01",
"cargo_type": "Glass",
"declared_value": 1000,
"user_id": 1
}
```
Управление тарифами

GET /rates/ - Получить список всех тарифов

POST /rates/ - Создать новый тариф

GET /rates/{rate_id} - Получить конкретный тариф

PUT /rates/{rate_id} - Обновить существующий тариф

DELETE /rates/{rate_id} - Удалить тариф

```json
Структура проекта
insurance-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── kafka_logger.py
│   └── api/
│       └── endpoints/
│           ├── __init__.py
│           ├── insurance.py
│           └── rates.py
│
├── tests/
│   └── test_main.py
│
├── alembic/
│   ├── versions/
│   └── alembic.ini
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Разработка

Для локальной разработки:
1. Создайте виртуальное окружение:

`python -m venv venv`

`source venv/bin/activate`

На Windows используйте 

`venv\Scripts\activate`

2. Установите зависимости

`pip install -r requirements.txt`

3. Запустите PostgreSQL и Kafka локально или измените 
`DATABASE_URL` и `KAFKA_BOOTSTRAP_SERVERS` в файле `.env` для использования удаленных сервисов.

4. Примените миграции базы данных:

`alembic upgrade head`

Запустите сервер для разработки:

`uvicorn app.main:app --reload`

Тестирование
Для запуска тестов используйте команду:

`pytest`

Логирование
Все изменения тарифов и расчеты страховых стоимостей логируются в Kafka. 

Убедитесь, что Kafka запущена и доступна перед использованием API.