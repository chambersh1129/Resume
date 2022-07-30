from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(f"{settings.ADMIN_URL_PREPEND}/admin/", admin.site.urls),
    path("api/", include("resume.api.urls")),
    path("graphql/", include("resume.graphql.urls")),
    path("health/", include("health_check.urls")),
    path("", include("resume.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
