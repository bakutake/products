import datetime
import random
import pytz

from django.core.management.base import BaseCommand

from sales.models import Order, OrderItem


class Command(BaseCommand):
    help = "Generates a given number of orders"

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="Indicates the number of orders to be created")

    def handle(self, *args, **kwargs):
        start_date = datetime.datetime(year=2018, month=1, day=1, hour=9, minute=0, tzinfo=pytz.UTC)
        total = kwargs.get("total")
        order_items = []

        try:
            for num_order in range(1, total+1):
                order = self._generate_order(num_order, start_date)
                order.save()

                for num_order_item in range(1, random.randint(1, 5)):
                    order_items.append(self._generate_order_item(order))

            OrderItem.objects.bulk_create(order_items)
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"An error has occurred: {ex}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Successfully created {total} orders"))

    def _generate_order(self, num_order, start_date):
        return Order(
            number=num_order,
            created_date=start_date + datetime.timedelta(hours=num_order)
        )

    def _generate_order_item(self, order):
        return OrderItem(
            order=order,
            product_name=f"Товар-{random.randint(1, 100)}",
            product_price=random.randint(100, 9999),
            amount=random.randint(1, 10),
        )
