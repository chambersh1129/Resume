from django.urls import path

from .views import (
    BootstrapView,
    BulmaAboutView,
    BulmaHobbyView,
    BulmaMilestoneDetailView,
    BulmaMilestoneTableView,
    BulmaMilestoneView,
    BulmaView,
    BulmaWorkHistoryView,
    HomePageView,
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
]
