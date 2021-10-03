# praktikum_new_diplom
![foodgram-project-react workflow](https://github.com/SanyaDeath/foodgram-project-react/actions/workflows/foodgram_main.yml/badge.svg)

Демоверсия сайта: <http://84.252.128.134>



Это проект Foodgram, сервис с возможностями:
- Регистрация пользователей,
- Создание, изменение и удаление репецптов.
- Фильтрация рецептов по тегам.
- Подписка на авторов и просмотр рецептов определенного автора.
- Добавление рецептов и формирование списка покупок для их приготовления.

---

Настроен Continuous Integration и Continuous Deployment для проекта Foodgram: автоматический запуск тестов, обновление образов на Docker Hub и автоматический деплой на боевой сервер при пуше в ветку main

---
### Технологии
- Python 3.8.5
- Django 3.0.5
- Docker-compose 3.7
- nginx 1.19.3
- postgres 12.4


<h3> Установка и развертывание </h3>
После выполнения push необходимо зайти на сервер

    $ ssh yc-user@<IP адрес>


### Установка докер
https://docs.docker.com/engine/install/

### Запуск проекта из директории infra
``` docker-compose up -d --build ```Shell

### Создание миграций приложения пользователей
```docker-compose exec backend python manage.py makemigrations users```Shell

### Создание миграций приложения рецептов
```docker-compose exec backend python manage.py makemigrations recipes```Shell

### Миграции
```docker-compose exec backend python manage.py migrate --noinput```Shell

### Сбор статики
```docker-compose exec backend python manage.py collectstatic --no-input```Shell

### Cоздания суперпользователя 
``` docker-compose exec backend python manage.py createsuperuser ```Shell

### Заполнения базы начальными данными
``` docker-compose exec backend python manage.py loaddata fixtures.json ```Shell

### Работал над проектом: Алексей Белов - ученик Яндекс.Практикум
https://hub.docker.com/repository/docker/sanyadeath/foodgram - dockerhub - dockerhub

http://84.252.128.134/admin/login/?next=/admin/ - облако 