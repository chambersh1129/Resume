from django.urls import path

from .views import BulmaView, HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    # path("bootstrap/", BootstrapView.as_view(), name="bootstrap"),
    path("bulma/", BulmaView.as_view(), name="bulma"),
]
