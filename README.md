# products

[Тестовое задание](https://github.com/bakutake/products/blob/master/python_test.txt)

## Установка

Использовался Python3.9.5 и Django версии 3.2.5.
Перед началом рекомендуется установить и запустить виртуальное окружение.
Далее нужно перейти из терминала (или консоли) в папку проекта.
После уствновить необходимые пакеты:

```bash
python -m pip install -r requirements.txt
```

Далее:
```bash
python manage.py migrate
python manage.py compilemessages
```

Для запуска сервера:

```bash
python manage.py runserver
```

## Management команда для генерации заказов

```bash
python manage.py generate_orders <total> # Сгенерирует <total> число заказов. Аргумент <total> является обязательным
```

## Отчеты

### Отчет по заказам за выбранный период времени

Отчет доступен будет по адресу /sales/ordersreport/
Примечание: datetimepicker не работает, и дату нужно будет ввести вручную (в формате "07/07/2021 17:07")

### Отчет по самым покупаемым товарам (Топ 20)

Отчет доступен будет по адресу /sales/topproductsreport/
Примечание: datetimepicker не работает, и дату нужно будет ввести вручную (в формате "07/07/2021 17:07")

## Информация о количестве запросов к БД

Реализировано через декоратор @query_counter, пример использования ниже, [код самого декоратора](https://github.com/bakutake/products/blob/master/sales/utils.py)

```python
class OrdersReportView(View):
    @query_counter
    def get(self, request):
        # обработка запроса
        # ...
```
