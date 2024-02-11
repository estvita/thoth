## Bitrix24 Integration Hub - Thoth

### Описание

Thoth позволяет создавать локальные приложения Битрикс24 с OAuth 2.0 авторизацией.

Одна инсталляция приложения позволяет интегрировать с Битрикс24 неограниченное количество независимых друг от друга внешних систем по API.

Токен OAuth 2.0 авторизации Битрикс24 автоматически обновляется.

## Виедоинструкция на Youtube -

https://youtu.be/Xy_UvvwiaGU

## Поддерживаемые системы
+ WhatsApp API [Business](https://developers.facebook.com/docs/whatsapp/) - текстовые сообщения, остальные типы в процессе
+ Telegram - в процессе
+ [Asterisk](https://docs.asterisk.org/) - в процессе

## Установка 
+ Для корректной работы платформы Thoth необходим домен, обеспеченный действительным SSL-сертификатом.
+ Пример настройки приложений [Flask с Gunicorn и Nginx на сервере Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04)
+ Все последующие действия должны осуществляться при запущенном и корректно работающем приложении.

## Генерация конфигурационного файла и подключение коннектора 
+ Запустите файл [add_config](tools/add_config.py)
~~~
python tools/add_config.py
~~~
+ Скрипт запросит необходимые для генерациии конфигурации данные
~~~
Введите название конфигурации (my_project): test
Введите адрес портала (domain.bitrix24.ru): domain.bitrix24.ru
Введите домен сервера, где будет расположен скрипт (domain.ru): domain.ru
~~~
+ В результате в папке configs будет сформирован конфигурационный файл, а в консоли будут выведены данные, необходимые для подключения к Битрикс24 и WhatsApp. 
Сохраните полученный ответ для удобства 
~~~
Базовая конфигурация сохранена. Данные для регистрации приложения:
1. Битрикс24. Путь вашего обработчика: https://domain.ru/bitrix?config=qJA0VBVH7tjxfGEfVE5U
2. Битрикс24. Путь для первоначальной установки: https://domain.ru/install?config=qJA0VBVH7tjxfGEfVE5U
3. Whatsapp. URL обратного вызова: https://domain.ru/whatsapp?config=qJA0VBVH7tjxfGEfVE5U
4. Whatsapp. Подтверждение маркера: tVjGYyPNCVfI8NnApDCZk33YY

~~~
+ В Битрикс24 создайте серверное локальное приложение без интерфейса в Битрикс24 и заполните соотвествующие поля (Путь вашего обработчика и Путь для первоначальной установки)
+ Необходимые права (Настройка прав): crm,imopenlines,contact_center,user,im,imconnector
+ Нажмите "Сохранить"
+ Конфигурационный файл будет автоматически заполнен данными с сервера Битрикс24
+ Скопируйте в соответствующие поля конфигурационного файла значения полей Код приложения (client_id) и Ключ приложения (client_secret)

#### Создание коннектора
+ Запустите файл [add_connector.py](tools/add_connector.py), выберите конфинурацию для настройки 
+ Введите имя коннектора и путь к файлу SVG или URL картинки

#### Подключение коннектора
+ Перейдите в разде Интеграции > Контакт Центр и выберите созданный коннектор
+ Нажмите "Подключить"
