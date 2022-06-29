from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

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
    SwaggerView,
    WorkHistoryViewSet,
)

resume_router = DefaultRouter()
resume_router.register("about", AboutMeViewSet)
resume_router.register("hobby", HobbyAPIViewSet)
resume_router.register("work_history", WorkHistoryViewSet)
resume_router.register("milestone", MilestoneAPIViewSet)

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
    path("api/openapi", get_schema_view(title="Resume API"), name="openapi-schema"),
    path("api/swagger/", SwaggerView.as_view(), name="swagger"),
    path("api/", include(resume_router.urls)),
]
