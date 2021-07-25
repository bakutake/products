from django.urls import path
from django.views.generic.base import RedirectView

from sales.views import OrdersReportView, TopProductsReportView


app_name = "sales"
urlpatterns = [
    path("ordersreport/", OrdersReportView.as_view(), name="orders_report"),
    path("topproductsreport/", TopProductsReportView.as_view(),
         name="top_products_report"),
    path("", RedirectView.as_view(url="/sales/ordersreport/")),
]
