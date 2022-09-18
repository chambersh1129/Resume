from django.urls import path

from .views import (
    BootstrapAboutView,
    BootstrapHobbyView,
    BootstrapMilestoneTableView,
    BootstrapMilestoneView,
    BootstrapView,
    BootstrapWorkHistoryView,
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
    path("bootstrap/about/", BootstrapAboutView.as_view(), name="bootstrap-about"),
    path("bootstrap/hobbies/", BootstrapHobbyView.as_view(), name="bootstrap-hobbies"),
    path("bootstrap/milestones/", BootstrapMilestoneView.as_view(), name="bootstrap-milestones"),
    path("bootstrap/milestones/table/", BootstrapMilestoneTableView.as_view(), name="bootstrap-milestone-table"),
    path("bootstrap/work_history/", BootstrapWorkHistoryView.as_view(), name="bootstrap-work-history"),
    path("bulma/", BulmaView.as_view(), name="bulma"),
    path("bulma/about/", BulmaAboutView.as_view(), name="bulma-about"),
    path("bulma/hobbies/", BulmaHobbyView.as_view(), name="bulma-hobbies"),
    path("bulma/milestones/", BulmaMilestoneView.as_view(), name="bulma-milestones"),
    path("bulma/milestones/table/", BulmaMilestoneTableView.as_view(), name="bulma-milestone-table"),
    path("bulma/milestones/<int:pk>/", BulmaMilestoneDetailView.as_view(), name="bulma-milestone-detail"),
    path("bulma/work_history/", BulmaWorkHistoryView.as_view(), name="bulma-work-history"),
]
