# mi-trainee-avito-test
Тестовое задание для стажера в юнит Market Intelligence (Avito)

## Стек: 
Python 3, Django 3, Django REST Framework, PostgreSQL, Docker, Gunicorn, Nginx, Unittest

### Описание
Это REST API сервиса для голосования. Например, для выбора самого популярного покемона.

Реализован пользовательский функционал дающий возможность пользоваться приложением не посещая сайт:
*	`POST /api/createPoll/` Создавать новые голосования с вариантами ответов.
*	`GET /api/poll/` Просматривать список доступных голосований. Натроена пагинация.
*	`PATCH /api/poll/poll_id/` Отдать свой голос за какой-либо вариант.
*	`GET /api/getResult/` Получить текущий результат голосования.

### Установка
- склонируйте проект с реппозитория GitHub
    ```
    git clone https://github.com/wiky-avis/mi-trainee-avito-test.git
    ```
- перейдите в директорию mi-trainee-avito-test/
    ```
    cd mi-trainee-avito-test/
    ```
- запустите docker-compose
    ```
    docker-compose up
    ```

### Использование
- зайдите на страницу http://localhost:8000/redoc/ 
и воспользуйтесь документацией к API :smile:
- зайдите на страницу http://localhost:8000/coverage/ 
чтобы посмотреть отчет coverage
- примеры запросов можно посмотреть в файле requests.http

### Дополнительные возможности
- заполнить базу тестовыми данными
    ```
    docker-compose run --rm web python manage.py loaddata db.json
    ```
- создать суперпользователя
    ```
    docker-compose run --rm web python manage.py createsuperuser
    ```
    
### Список работ и порядок выполнения задания:
- Создание и настройка проекта
- Создание моделей
- настройка отображения моделей в панели администратора
- api для создания голосования с вариантами ответов
- api для голосования за конкретный вариант
- api для для просмотра результата по конкретному голосованию
- документация к api
- подключение базы PostgreSQL
- tests.test_models
- tests.test_urls
- tests.test_views.py
- coverage report
- docker
- db.json
- README.md
