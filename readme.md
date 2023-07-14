
# Мессенджер на Джанго и JavaScript
## с применением Channels, DRF, NodeJS, HTML, CSS
____
### Установка приложения
____
Клонируем проект с репозитория 

```
git clone https://github.com/molodcovnik/SF_AJAX.git
pip install -r requirements.txt
venv\scripts\activate
(venv): cd src
```

Открываем еще один терминал для Redis.

```
redis-server
```

Если сервер не запускается, делаем следующее:

```
redis-cli
shutdown
exit
```

И запускаем заново

```
redis-server
```

В первом терминале запускаем проект:

```
python manage.py runserver
```

Переходим по ссылке:

http://127.0.0.1:8000/chat/

---

Для проверки функционала есть 4 пользователя:

Inna

Nik

Maria

Tim

Пароли у всех одинаковые: 123456789K!

----

Залогиниться можно по ссылке:

http://127.0.0.1:8000/accounts/login/

Далее заходим с разных пользователей, разных браузеров и ведем переписку))


![login](src/media/images/login.png)


Попадаем на главную страницу, где видно всех пользователей и все ваши чаты

![index](src/media/images/index.png)

Можно посмотреть всех пользователей и отредактировать информацию о себе

![edit_info](src/media/images/edit-profile.png)

При нажатии на другого пользователя создается чат с ним

![chat-room](src/media/images/room-page.png)

Чат изначально создается на двух пользователей, при желании можно добавить неограниченное количество юзеров в этот чат.

