# Проект API для Yatube

Проект `api_final_yatube` представляет собой API для сервиса Yatube, позволяющий обмениваться информацией между Yatube и другими сервисами.

## Описание

API включает следующие эндопинты:
```
api/v1/posts/
api/v1/posts/{id}/
api/v1/posts/{post_id}/comments/
api/v1/posts/{post_id}/comments/{comment_id}
api/v1/groups/
api/v1/groups/{id}/
api/v1/follow/
```
Эти эндпоинты предназначены для работы с моделями Post, Comment, Group и Follow. В проекте используется авторизация с помощью JWT-токена. Для получения постов реализована пагинация LimitOffset, также возможен поиск по подпискам.

## Установка

1. Клонируйте репозиторий и перейдите в папку проекта:

```
git clone https://github.com/DayKotya/api_final_yatube
```

```
cd api_final_yatube
```

2) Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

3) Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4) Выполните миграции:

```
python3 manage.py migrate
```

5) Запустите проект:

```
python3 manage.py runserver
```

## Примеры

Пример авторизации с помощью JWT-токена:

отправляем POST-запрос на http://127.0.0.1:8000/api/v1/jwt/create/, передав логин и пароль в полях "username" и "password":
```
{
"username": "string",
"password": "string"
}
```
ответ:
```
{
"refresh": "string",
"access": "string"
}
```

Пример создания нового поста с помощью POST-запроса:

отправляем POST-запрос на http://127.0.0.1:8000/api/v1/posts/:
```
{
"text": "string",
"image": "string",
"group": 0
}
```
ответ:
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
Пример получения списка публикаций с помощью GET-запроса:

отправляем GET-запрос на http://127.0.0.1:8000/api/v1/posts/ и получаем ответ:
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```

Обратите внимание, что это только примеры, и вы можете вносить изменения согласно вашим предпочтениям.

