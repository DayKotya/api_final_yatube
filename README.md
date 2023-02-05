### Описание

Проект api_final_yatube представляет собой API для сервиса yatube. API удобно использовать для обмена информацией между yatube и другими сервисами.
В проекте описаны эндопинты:
```
api/v1/posts/
api/v1/posts/{id}/
api/v1/posts/{post_id}/comments/
api/v1/posts/{post_id}/comments/{comment_id}
api/v1/groups/
api/v1/groups/{id}/
api/v1/follow/
```
Данные эндпоинты используются для взаимодействия с моделями Post, Comment, Group, Follow.
В проекте используется авторизация с помощью JWT-токена.
В проекте для получения постов используется LimitOffSet пагинация, возможен поиск по подпискам - Follow.

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DayKotya/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры

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