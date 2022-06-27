from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from .views.api_views import AboutMeViewSet, HobbyAPIViewSet, JobRoleViewSet, MilestoneAPIViewSet, SwaggerView
from .views.views import BootstrapView, BulmaView, HomePageView

resume_router = DefaultRouter()
resume_router.register("about", AboutMeViewSet)
resume_router.register("hobby", HobbyAPIViewSet)
resume_router.register("role", JobRoleViewSet)
resume_router.register("milestone", MilestoneAPIViewSet)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("bootstrap/", BootstrapView.as_view(), name="bootstrap"),
    path("bulma/", BulmaView.as_view(), name="bulma"),
    path("api/openapi", get_schema_view(title="Resume API"), name="openapi-schema"),
    path("api/swagger/", SwaggerView.as_view(), name="swagger"),
    path("api/", include(resume_router.urls)),
]
