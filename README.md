# NewsAPI - новостной сервис 📰

## Описание проекта:
#### Инструменты: Django, Django Rest Framework, PostgreSQL, Docker, Gunicorn, Nginx
---
Данный сервис позволит вам размещать новости, комментировать и лайкать посты других пользователей.

Редактировать посты и удалять может владелец поста и админ.

Удалять комментарии может владелец поста, владелец комментария, админ.

Проект доступен по адресу : 
https://newsapi.ddns.net/

Регистрация пользователей через админку:
```
/admin/
```
login: admin

password: admin

## Как использовать проект:

Для того, чтобы пользоваться сервисом необходимо пройти процесс аутентификации(реализована кастомная аутентификация).

---
### /api/v1/auth/ [POST]

Пример запроса:

request:
```
{
    "username": "test",
    "password": "test"
}
```
response:
```
{
    "token": "a0s97d09ahdj-9as-d-daawdmslkv"
}
```

В заголовках к остальным эндпоинтам передаем
```
Authorization : 'Token a0s97d09ahdj-9as-d-daawdmslkv'
```
---
### /api/v1/news/ [GET, POST]

GET response:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "first admin news",
            "text": "hello there",
            "author": "admin",
            "is_fan": false,
            "comments_amount": 0,
            "likes_amount": 0,
            "comments": []
        }
    ]
}
```
POST request:
```
{
    "title": "test1title",
    "text": "test1text"
}
```


POST response:
```
{
    "id": 2,
    "title": "test1title",
    "text": "test1text",
    "author": "test1",
    "is_fan": false,
    "comments_amount": 0,
    "likes_amount": 0,
    "comments": []
}
```
---
### /api/v1/news/\<id\>/ [GET, PUT, PATCH, DELETE]

GET response:
```
{
    "id": 2,
    "title": "test1title",
    "text": "test1text",
    "author": "test1",
    "is_fan": true,
    "comments_amount": 0,
    "likes_amount": 1,
    "comments": []
}
```

PUT request:
```
{
    "title": "puttitle",
    "text":"puttext"
}
```

PUT response:
```
{
    "id": 2,
    "title": "puttitle",
    "text": "puttext",
    "author": "test1",
    "is_fan": true,
    "comments_amount": 0,
    "likes_amount": 1,
    "comments": []
}
```

PATCH request:
```
{
    "title": "patch"
}
```

PATCH response:
```
{
    "id": 2,
    "title": "patch",
    "text": "puttext",
    "author": "test1",
    "is_fan": true,
    "comments_amount": 0,
    "likes_amount": 1,
    "comments": []
}
```

DELETE response:
```
{
    "detail": "Post has been deleted successfully."
}
```
---
### /api/v1/news/\<id\>/comments/ [GET, POST]

POST request:
```
{
    "text": "test1text"
}
```

POST response:
```
{
    "id": 1,
    "text": "test1text",
    "author": "test1"
}
```

GET response:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "text": "test1text",
            "author": "test1"
        }
    ]
}
```
---
### /api/v1/news/\<id\>/comments/\<id\>/ [GET, DELETE]

GET response:
```
{
    "id": 1,
    "text": "test1text",
    "author": "test1"
}
```

DELETE response:
```
{
    "detail": "Comment has been deleted successfully."
}
```
---
### /api/v1/news/\<id\>/like/ [GET]

GET response:
```
{
    "detail": "Liked successfully."
}
```
---
### /api/v1/news/\<id\>/unlike/ [GET]

GET response:
```
{
    "detail": "Unliked successfully."
}
```
---
## Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/we5h/drf_news.git
```

- Установить Docker:

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

либо Docker Desktop для вашей платформы:
https://docs.docker.com/engine/install/

- Запустить проект в сети контейнеров docker compose:

`docker compose up --build -d`

- Зайти в контейнер, открыть bash:

`docker compose exec backend bash`

- Перейти в каталог backend, где находится manahe.py, создать миграции:

`python3 manage.py migrate`

- Создать суперпользователя:

`python3 manage.py createsuperuser`

- Собрать статику и скопировать в общий volume:

`python3 manage.py collectstatic`

`cp -r /app/collected_static/. /backend_static/`

`cp -r /app/index/. /backend_static/`


- Проект доступен по адресу 127.0.0.1:8000
---
Автор:
* [Dmitrij Gribkov](https://github.com/we5h)
