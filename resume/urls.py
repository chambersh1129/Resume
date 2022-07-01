from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from .views import (
    AboutMeViewSet,
    BootstrapView,
    BulmaAboutView,
    BulmaHobbyView,
    BulmaMilestoneDetailView,
    BulmaMilestoneTableView,
    BulmaMilestoneView,
    BulmaView,
    BulmaWorkHistoryView,
    HobbyAPIViewSet,
    HomePageView,
    MilestoneAPIViewSet,
    TagAPIViewSet,
    WorkHistoryAPIViewSet,
)

resume_router = DefaultRouter()
resume_router.register("hobby", HobbyAPIViewSet)
resume_router.register("milestone", MilestoneAPIViewSet)
resume_router.register("milestone/tags", TagAPIViewSet)
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
    path("", HomePageView.as_view(), name="home"),
    path("bootstrap/", BootstrapView.as_view(), name="bootstrap"),
    path("bulma/", BulmaView.as_view(), name="bulma"),
    path("bulma/about/", BulmaAboutView.as_view(), name="bulma-about"),
    path("bulma/hobbies/", BulmaHobbyView.as_view(), name="bulma-hobbies"),
    path("bulma/milestones/", BulmaMilestoneView.as_view(), name="bulma-milestones"),
    path("bulma/milestones/table/", BulmaMilestoneTableView.as_view(), name="bulma-milestone-table"),
    path("bulma/milestones/<int:pk>/", BulmaMilestoneDetailView.as_view(), name="bulma-milestone-detail"),
    path("bulma/work_history/", BulmaWorkHistoryView.as_view(), name="bulma-work-history"),
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("api/about_me", AboutMeViewSet.as_view(), name="about-me"),
    path("api/", include(resume_router.urls)),
]
