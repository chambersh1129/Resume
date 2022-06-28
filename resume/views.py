from django.db.models import Q
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from django.views.generic.detail import DetailView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import AboutMe, Hobby, Milestone, WorkHistory
from .serializers import AboutMeSerializer, HobbySerializer, MilestoneSerializer, WorkHistorySerializer


class AboutAbstractView(TemplateView):
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["about"] = AboutMe.objects.first()
    #     return context

    def dispatch(self, request, *args, **kwargs):
        self.about = AboutMe.objects.first()
        response = super(AboutAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class HobbyAbstractView(TemplateView):
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["hobbies"] = Hobby.objects.all()
    #     return context

    def dispatch(self, request, *args, **kwargs):
        self.hobbies = Hobby.objects.all()
        response = super(HobbyAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class MilestoneAbstractView(TemplateView):
    OFFSET = 0
    LIMIT = 10

    def _get_queryset(self, params):
        query_list = []

        if "name" in params:
            query_list.append(Q(name__icontains=params.get("name")))

        if "type" in params:
            query_list.append(Q(type__icontains=params.get("type")))

        if "tag" in params:
            query_list.append(Q(tag__tag__icontains=params.get("tag")))

        return query_list

    def dispatch(self, request, *args, **kwargs):
        try:
            offset = int(request.GET.get("offset", self.OFFSET))

        except Exception:
            offset = self.OFFSET

        try:
            limit = int(request.GET.get("limit", self.LIMIT))

        except Exception:
            limit = self.LIMIT

        query_list = self._get_queryset(request.GET)
        if query_list:
            query = Milestone.objects.filter(*query_list).distinct()

        else:
            query = Milestone.objects.all()

        total_count = query.count()
        if total_count > (offset + limit):
            self.next_page = f"?offset={offset+limit}"

        if offset:
            self.prev_page = f"?offset={offset-limit}"

        max = offset + limit

        self.milestones = query[offset:max]

        self.milestone_types = dict(zip(Milestone.TypeChoices.values, Milestone.TypeChoices.labels))

        response = super(MilestoneAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class WorkHistoryAbstractView(TemplateView):
    OFFSET = 0
    LIMIT = 3

    def dispatch(self, request, *args, **kwargs):
        try:
            offset = int(request.GET.get("offset", self.OFFSET))

        except Exception:
            offset = self.OFFSET

        try:
            limit = int(request.GET.get("limit", self.LIMIT))

        except Exception:
            limit = self.LIMIT

        total_count = WorkHistory.objects.count()
        if total_count > (offset + limit):
            self.next_page = f"?offset={offset+limit}"

        max = offset + limit

        self.work_history = WorkHistory.objects.all()[offset:max]

        response = super(WorkHistoryAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class URLAbstractView(TemplateView):
    # exclude_links = []

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["links"] = [
    #         {"page": "Bootstrap", "url": reverse("bootstrap")},
    #         {"page": "Bulma", "url": reverse("bulma")},
    #         {"page": "API Docs", "url": reverse("swagger")},
    #     ]
    #     context["exclude_links"] = self.exclude_links
    #     return context

    def dispatch(self, request, *args, **kwargs):
        self.links = [
            {"page": "Bootstrap", "url": reverse("bootstrap")},
            {"page": "Bulma", "url": reverse("bulma")},
            {"page": "API Docs", "url": reverse("swagger")},
        ]
        response = super(URLAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class HomePageView(RedirectView):
    permanent = True
    pattern_name = "bulma"


class BootstrapView(AboutAbstractView, URLAbstractView):
    template_name = "resume/bootstrap/base.html"


class BulmaView(AboutAbstractView, URLAbstractView):
    template_name = "resume/bulma/base.html"


class BulmaAboutView(AboutAbstractView):
    template_name = "resume/bulma/about.html"


class BulmaHobbyView(HobbyAbstractView):
    template_name = "resume/bulma/hobbies.html"


class BulmaMilestoneView(MilestoneAbstractView):
    template_name = "resume/bulma/milestones.html"


class BulmaMilestoneDetailView(DetailView):
    template_name = "resume/bulma/milestone_detail.html"
    model = Milestone

    def dispatch(self, request, *args, **kwargs):
        response = super(BulmaMilestoneDetailView, self).dispatch(request, *args, **kwargs)
        response["HX-Trigger-After-Settle"] = "openModal"
        return response


class BulmaWorkHistoryView(WorkHistoryAbstractView):
    template_name = "resume/bulma/work_history.html"


"""
API Views
"""


class ListViewSet(GenericViewSet, ListModelMixin):
    pass


class AboutMeViewSet(ListViewSet):
    """
    Get information about me, including contact information
    """

    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class HobbyAPIViewSet(ListViewSet):
    """
    What I like to do when I'm not working
    """

    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer


class WorkHistoryViewSet(ListViewSet):
    """
    My work history, including my current position (if I'm still employeed)
    """

    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer


class MilestoneAPIViewSet(ListViewSet):
    """
    What I consider my major milestones.  Includes projects, certifications, eduction, or anything else I consider
    an accomplishment
    """

    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer


class SwaggerView(TemplateView):
    template_name = "resume/swagger.html"
    extra_context = {"schema_url": "openapi-schema"}
