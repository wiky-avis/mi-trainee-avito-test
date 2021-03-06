# mi-trainee-avito-test
Тестовое задание для стажера в юнит Market Intelligence (Avito)

## Стек: 
Python 3, Django 3, Django REST Framework, PostgreSQL, Docker, Gunicorn, Nginx, Unittest

## Описание:
Это REST API сервиса для голосования. Например, для выбора самого популярного покемона.

Реализован пользовательский функционал дающий возможность пользоваться приложением не посещая сайт:
*	`POST /api/v1/createPoll/` Создавать новые голосования с вариантами ответов.
*	`GET /api/v1/poll/` Просматривать список доступных голосований. Натроена пагинация.
*	`PATCH /api/v1/poll/<poll_id>/` Отдать свой голос за какой-либо вариант.
*	`GET /api/v1/getResult/<poll_id>/` Получить текущий результат голосования.

## Схема данных:

![GitHub Logo](/media/images_for_git/schema.jpg)

## Установка:
- Склонируйте проект с реппозитория GitHub
    ```
    git clone https://github.com/wiky-avis/mi-trainee-avito-test.git
    ```
- Перейдите в директорию mi-trainee-avito-test/
    ```
    cd mi-trainee-avito-test/
    ```
- Запустите docker-compose
    ```
    docker-compose up
    ```

## Использование:
- Документация к API http://localhost:8000/redoc/ 
- Запуск тестов
    ```
    docker-compose run --rm web python manage.py test
    ```
- Отчет с оценкой тестового покрытия на проекте http://localhost:8000/coverage/
- Создать суперпользователя
    ```
    docker-compose run --rm web python manage.py createsuperuser
    ```
- Заполнить базу тестовыми данными
    ```
    docker-compose run --rm web python manage.py loaddata db.json
    ```
    
## Примеры запросов к API:
Для формирования ответов и запросов будет использовано расширение для VS Code [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

### Создаем голосование с тремя вариантами ответов:
Отправляем POST-запрос на адрес http://localhost:8000/api/v1/createPoll/.

![GitHub Logo](/media/images_for_git/create_poll.jpg)

### Запрашиваем список доступных голосований:
Отправляем GET-запрос на адрес http://localhost:8000/api/v1/poll/.

![GitHub Logo](/media/images_for_git/polls_all.jpg)

### Отдаем свой голос за вариант ответа у которого id 2 в голосовании c id 1:
Отправляем PATCH-запрос на адрес http://localhost:8000/api/v1/poll/1/.

![GitHub Logo](/media/images_for_git/vote.jpg)

### Запрашиваем результат голосования c id 1:
Отправляем GET-запрос на адрес http://localhost:8000/api/v1/getResult/1/.

![GitHub Logo](/media/images_for_git/get_result.jpg)
