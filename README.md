# Minicart

minicart -- это веб-приложение для осуществления покупок тех или иных продуктов в тестовом режиме, написанное на Django с использованием Stripe API.

Приложение содержит Django-модель `Item` с полями: `name`, `description`, `price`. Список всех продуктов, содержащихся в базе можно просмотреть по соответствующему запросу `GET /items`. Добавление, модификация и удаление продуктов может быть осуществлено через панель администратора.

API данного веб-приложения содержит два ключевых метода:

1. `GET /buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного `Item`. При выполнении этого метода c бэкенда с помощью python библиотеки `stripe` должен выполняться запрос `stripe.checkout.Session.create(...)` и полученный `session.id` выдаваться в результате запроса

2.	`GET /item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном `Item` и кнопка `Buy`. По нажатию на кнопку `Buy` должен происходить запрос на `/buy/{id}`, получение `session_id` и далее  с помощью JS библиотеки `Stripe` происходить редирект на Checkout форму `stripe.redirectToCheckout(sessionId=session_id)`

## Бонусные цели

1. [ ] Запуск используя Docker
2. [x] Использование environment variables
3. [x] Просмотр Django Моделей в Django Admin панели
4. [ ] Запуск приложения на удаленном сервере, доступном для тестирования
5. [x] Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
6. [ ] Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
7. [ ] Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
8. [ ] Реализовать не Stripe Session, а Stripe Payment Intent.

## Пример

API метод для получения HTML c кнопкой на платежную форму от Stripe для Item с id=1:

```sh
curl -X GET http://localhost:8000/item/1
```

Результат - HTML c инфой и кнопкой:

```html
<html>
  <head>
    <title>Buy Item 1</title>
  </head>
  <body>
    <h1>Item 1</h1>
    <p>Description of Item 1</p>
    <p>1111</p>
    <button id="buy-button">Buy</button>
    <script type="text/javascript">
      var stripe = Stripe('pk_test_a9nwZVa5O7b0xz3lxl318KSU00x1L9ZWsF');
      var buyButton = document.getElementById(buy-button');
      buyButton.addEventListener('click', function() {
        // Create a new Checkout Session using the server-side endpoint 
        // Redirect to Stripe Session Checkout
        fetch('/buy/1', {method: 'GET'})
        .then(response => return response.json())
        .then(session => stripe.redirectToCheckout({ sessionId: session.id }))
      });
    </script>
  </body>
</html>
```

## Запуск

Приложение может быть запущено при помощи вызова следующей команды:

```sh
python .\minicart\manage.py runserver
```

В результате будет локально запущен сервер, который будет принимать запросы на адрес `localhost:8000` по умолчанию:

```sh
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 24, 2023 - 17:50:44
Django version 4.1.2, using settings 'minicart.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Использование

Данное веб-приложение было развернуто и опубликовано на [railway.app](https://railway.app) и доступно по ссылке: [minicart-app](https://minicart-deploy-production.up.railway.app/), а также в разделе Releases. В развернутой на серевере PostgreSQL базе данных был создан супер-пользователь со следующими данными:

```
Username: admin
Email address: example@test.org
Password: 123123
```

Используя эти данные, может быть осуществлен вход в панель администратора приложения Django, в котором можно редактировать, добавлять и удалять объекты существующих в проекте моделей.
