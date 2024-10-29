Этот проект состоит из двух частей:

1. **Серверная часть (API)**: Предоставляет API для CRUD операций над товарами, типами и ценами.
2. **Клиентская часть (Интернет-магазин)**: Использует API для отображения товаров и взаимодействия с ними.

## Технологический стек

- Python 3.9
- Django 3.2
- Django REST Framework 3.12
- Docker
- Docker Compose

## Установка и запуск

### 1. Клонирование репозитория

Склонируйте репозиторий на ваш локальный компьютер:

git clone https://github.com/ZHNEC77/service
cd service


### 2. Установка зависимостей
Перейдите в директорию db_server и установите зависимости:

cd db_server
pip install -r requirements.txt

Перейдите в директорию shop_client и установите зависимости:

cd ../shop_client
pip install -r requirements.txt


### 3. Применение миграций
Перейдите в директорию db_server и примените миграции:

cd ../db_server
python manage.py makemigrations
python manage.py migrate


### 4. Запуск сервера
Запустите серверную часть (API):

cd ../db_server
python manage.py runserver 0.0.0.0:8000

Запустите клиентскую часть:

cd ../shop_client
python manage.py runserver 0.0.0.0:8001


### 5. Запуск с использованием Docker
docker-compose up --build


После успешного запуска, серверная часть будет доступна по адресу http://localhost:8000, а клиентская часть — по адресу http://localhost:8001.

Использование
### Серверная часть (API)
GET /api/products/ - Получить список всех товаров.

POST /api/products/ - Создать новый товар.

GET /api/products/{id}/ - Получить информацию о конкретном товаре.

PUT /api/products/{id}/ - Обновить информацию о товаре.

DELETE /api/products/{id}/ - Удалить товар.

POST /api/products/{id}/decrease_quantity/ - Уменьшить количество товара на складе.



### Клиентская часть
GET /products/ - Получить список всех товаров.

GET /products/{id}/ - Получить информацию о конкретном товаре.

POST /products/{id}/decrease_quantity/ - Уменьшить количество товара на складе.


### Админ-панель
Админ-панель для серверной части доступна по адресу http://localhost:8000/admin/. Для доступа к админ-панели создайте суперпользователя:

cd db_server
python manage.py createsuperuser
