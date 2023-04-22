## Configuration

admin: root <br>
password: root

#### Все последующие пользователи имеет одинаковый username и password

## How to run project

1. Измените под себя базу данных
    - Это можно сделать зайдя в **core/settings.py** и изменить ключи и значения словаря INSTALLED_APPS
2. Примените миграций
   > `python3 manage.py migrate`
3. Примените фиксутры
    - Применить фикстуры нужно все вместе
    > `python3 manage.py loaddata fixtures/users.json fixtures/permissions.json fixtures/photos.json`

4. Запустить проект
    > `python3 manage.py runserver`
