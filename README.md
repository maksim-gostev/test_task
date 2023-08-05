# Тестовое задание "Процесс «Птицы»"

# Стек технологий

- [Python 3.10](https://www.python.org/)
- [Django 4.2.2](https://www.djangoproject.com/)
- [Django REST Framework 3.14.0](https://www.django-rest-framework.org/)
- [Poetry](https://python-poetry.org/)
- [pytest-django](https://pytest-django.readthedocs.io/en/latest/index.html)
- [drf-spectacular](https://pypi.org/project/drf-spectacular/)

### Функционал
>* Список птиц: http://127.0.0.1:8000/bird/
>* Для отображения списка птиц использовать кастомные списки
>* Карточка птицы: http://127.0.0.1:8000/bird/<int:pk>/
>* Создание новой птицы: http://127.0.0.1:8000/bird/create/
>* При создании птицы возможно сохранить фото
>* Добавить процесс «Птицы которых я видел»
>* - Юзер кейс: В списке птиц выбирается карточка птицы которую увидел пользователь, пользователь переходит к 
     самой карточке и может нажать на кнопку «Видел».
>- http://127.0.0.1:8000/saw/<int:pk>/
>-   Идентификатор объекта сохраняется в глобальной переменной. 
     После, пользователь переходит в раздел «Птицы которых я видел»
>- http://127.0.0.1:8000/saw/
>-  нажимает на кнопку «+». 
>-  http://127.0.0.1:8000/saw/<int:pk>/ metod POST
>-  Из глобальной переменной
     получается ИД объекта, автоматически создается запись с: 
>* - Текущее время и дата
>* - Фото птицы из БД
>* - Количество актов видения птицы на момент создания записи
>*  Добавлен сваггер
>* http://127.0.0.1:8000/api/swagger