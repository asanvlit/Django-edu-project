# 🔮  Yartone. Платформа для художников

 Проект, выполненный в рамках модуля "Принципы работы серверной части платформ управления данными. Контроль версий" онлайн курса  Казанского федерального университета

## Использованные технологии:

* Django, Django REST
* PostgreSQL
* Redis

## Запуск проекта для разработки:

*MacOS, Linux*:
* `python3 -m venv venv` - создание виртуального окружения
* `source venv/bin/activate` - войти в виртуальное окружение
* `pip install -r requirements.txt` - установка зависимостей
* `python manage.py migrate` - примененить миграции
* `python manage.py runserver` - запустить сервер для разработки на http://127.0.0.1:8000

*Windows*:
* `python -m venv venv` - создание виртуального окружения
* `venv/Scripts/Activate.ps1` - войти в виртуальное окружение
* `pip install -r requirements.txt` - установка зависимостей
* `python manage.py migrate` - примененить миграции
* `python manage.py runserver` - запустить сервер для разработки на http://127.0.0.1:8000

## Функционал проекта:

* Создание, редактирование, удаление и просмотр постов
* Создание и добавление тегов к постам
* Просмотр постов других пользователей
* Подписки на пользователей

* Аналитика по постам пользователя
* Экспорт и импорт постов в csv формате
* Статистика по посещению страниц

## Дополнительные возможности:

* Кэширование с помощью Redis

