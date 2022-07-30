from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from .views import AboutMeViewSet, HobbyAPIViewSet, MilestoneAPIViewSet, TagAPIViewSet, WorkHistoryAPIViewSet

resume_router = DefaultRouter()
resume_router.register("hobbies", HobbyAPIViewSet)
resume_router.register("milestones", MilestoneAPIViewSet)
resume_router.register("milestones/tags", TagAPIViewSet)
resume_router.register("work_history", WorkHistoryAPIViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Resume API",
        description="Resume for Hunter Chambers",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    path("about_me/", AboutMeViewSet.as_view(), name="about-me"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api-docs"),
    path("", include(resume_router.urls)),
]
