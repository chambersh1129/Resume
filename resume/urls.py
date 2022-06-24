from django.urls import path

from .views import AlpineView, BootstrapView, HomePageView, BulmaView, TailWindView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("alpine/", AlpineView.as_view(), name="alpine"),
    path("bootstrap/", BootstrapView.as_view(), name="bootstrap"),
    path("bulma/", BulmaView.as_view(), name="bulma"),
    path("tailwind/", TailWindView.as_view(), name="tailwind"),
]
