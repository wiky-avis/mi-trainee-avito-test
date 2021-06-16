# mi-trainee-avito-test
Тестовое задание для стажера в юнит Market Intelligence (Avito)


### Описание
Это REST API для сервиса для голосования. Например, для выбора самого популярного покемона.

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

### Дополнительные возможности
- заполнить базу тестовыми данными
    ```
    docker-compose run --rm web python manage.py loaddata db.json
    ```
- создать суперпользователя
    ```
    docker-compose run --rm web python manage.py createsuperuser
    ```
