from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from sales.models import Order, OrderItem
from sales.forms import TimeIntervalForm
from sales.utils import query_counter


class OrdersReportView(View):
    @query_counter
    @csrf_exempt
    def get(self, request):
        time_interval_form = TimeIntervalForm(request.GET)
        if not time_interval_form.is_valid():
            return render(request, "sales/orders_report.html",
                          context={"time_interval_form": time_interval_form})
        start_date = time_interval_form.cleaned_data["start_date"]
        end_date = time_interval_form.cleaned_data["end_date"]

        orders = (Order.objects
                  .filter(created_date__range=(start_date, end_date))
                  .prefetch_related("orderitem_set")
                  )
        orders_result = []
        for order in orders:
            order_price = 0
            order_items = []
            for order_item in order.orderitem_set.all():
                order_items.append(f"{order_item.product_name} x {order_item.amount}")
                order_price += order_item.product_price * order_item.amount
            orders_result.append({
                "created_date": order.created_date,
                "number": order.number,
                "order_price": order_price,
                "order_items": order_items,
            })
        return render(request, "sales/orders_report.html",
                      context={"orders": orders_result,
                               "time_interval_form": time_interval_form})


class TopProductsReportView(View):
    def get(self, request):
        pass

    def _order_items_to_dict_format(self, order_items):
        return {order_item["product_name"]: order_item["total"] for order_item in order_items}
