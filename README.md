````markdown
# FastAPI CRUD

Простой проект на **FastAPI + SQLAlchemy + Pydantic**.  
Реализован CRUD для пользователей и постов.

## Установка
```bash
git clone https://github.com/jasperBLCK/FastAPI-CRUD.git
cd FastAPI-CRUD
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
````

## Запуск

```bash
uvicorn main:app --reload
```

Документация API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Эндпоинты

### Пользователи

* `POST /users` — создать пользователя
* `GET /users` — список пользователей
* `DELETE /users` — удалить пользователя (по имени и паролю)

### Посты

* `POST /contents` — создать пост
* `GET /contents` — список постов
* `PUT /contents/{content_id}` — обновить пост
* `DELETE /contents/{content_id}` — удалить пост

```
