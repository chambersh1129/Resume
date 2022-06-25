from django.urls import path

from .views import BootstrapView, BulmaView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("bootstrap/", BootstrapView.as_view(), name="bootstrap"),
    path("bulma/", BulmaView.as_view(), name="bulma"),
]
