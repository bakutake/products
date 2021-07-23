from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    number = models.IntegerField(_("sales.order.number"))
    created_date = models.DateTimeField(_("sales.order.created_date"))

    def __str__(self):
        return f"Order {self.number} created at {self.created_date}"

    class Meta:
        verbose_name = _("sales.order")
        verbose_name_plural = _("sales.orders")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name=_("sales.order_item.order"))
    product_name = models.CharField(_("sales.order_item.created_date"),
                                    max_length=100)
    product_price = models.DecimalField(_("sales.order_item.product_price"),
                                        max_digits=15, decimal_places=2)
    amount = models.IntegerField(_("sales.order_item.amount"))

    def __str__(self):
        return f"Order {self.order.number} - {self.product_name} ({self.amount} pcs.) by price {self.product_price}"

    class Meta:
        verbose_name = _("sales.order_item")
        verbose_name_plural = _("sales.order_items")
