from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path("sales/", include("sales.urls")),
    path("", RedirectView.as_view(url="/sales/"), name="main_page"),
]
