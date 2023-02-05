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

Пример создания пользователя с помощью JWT-токена:

отправляем
```
фывфыв
```

