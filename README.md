# API для Yatube

API для социальной сети Yatube. Через него можно читать публикации,
создавать и редактировать свои посты, оставлять комментарии, просматривать
группы и подписываться на авторов. Для изменения данных используется
JWT-аутентификация.

## Технологии

- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite

## Установка

Клонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone <адрес_репозитория>
cd api-final-yatube-ad
```

Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Выполните миграции и запустите сервер:

```bash
cd yatube_api
python manage.py migrate
python manage.py runserver
```

Документация API будет доступна по адресу
`http://127.0.0.1:8000/redoc/`.

## Примеры запросов

Получить список публикаций:

```http
GET /api/v1/posts/
```

Создать публикацию:

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Новая публикация",
  "group": 1
}
```

Получить JWT-токен:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "username",
  "password": "password"
}
```

Подписаться на автора:

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "following": "author_username"
}
```
