from django.db.models import Q
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from django.views.generic.detail import DetailView

from .models import AboutMe, Hobby, Milestone, Tag, WorkHistory


class AboutAbstractView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.about = AboutMe.objects.first()
        response = super(AboutAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class HobbyAbstractView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.hobbies = Hobby.objects.all()
        response = super(HobbyAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class MilestoneAbstractView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.milestone_types = Milestone.TypeChoices
        self.tags = list(Tag.objects.all().values_list("tag", flat=True))
        response = super(MilestoneAbstractView, self).dispatch(request, *args, **kwargs)
        return response


class MilestoneDetailAbstractView(DetailView):
    HX_TRIGGER = None

    def dispatch(self, request, *args, **kwargs):
        response = super(MilestoneDetailAbstractView, self).dispatch(request, *args, **kwargs)
        if self.HX_TRIGGER:
            response["HX-Trigger-After-Settle"] = self.HX_TRIGGER
        return response


class MilestoneTableAbstractView(TemplateView):
    OFFSET = 0
    LIMIT = 10

    def _get_queryset(self, params):
        query_filter = []
        get_params = ""

        if "milestone" in params:
            param = params.get("milestone")
            query_filter.append(Q(name__icontains=param))
            get_params += f"&milestone={param}"

        if "desc" in params:
            param = params.get("desc")
            query_filter.append(Q(description__icontains=param))
            get_params += f"&desc={param}"

        if "type" in params:
            param = params.get("type")
            query_filter.append(Q(type__icontains=param))
            get_params += f"&type={param}"

        if "tag" in params:
            param = params.get("tag")
            query_filter.append(Q(tag__tag__icontains=param))
            get_params += f"&tag={param}"

        return query_filter, get_params

    def dispatch(self, request, *args, **kwargs):
        try:
            offset = int(request.GET.get("offset", self.OFFSET))

        except Exception:
            offset = self.OFFSET

        try:
            limit = int(request.GET.get("limit", self.LIMIT))

        except Exception:
            limit = self.LIMIT

        query_filter, get_params = self._get_queryset(request.GET)

        if query_filter:
            query = Milestone.objects.filter(*query_filter).distinct()

        else:
            query = Milestone.objects.all()

        self.total_count = query.count()
        if self.total_count > (offset + limit):
            self.next_page = f"?offset={offset+limit}"
            if get_params:
                self.next_page += get_params

        if offset:
            self.prev_page = f"?offset={offset-limit}"
            if get_params:
                self.prev_page += get_params

        max = offset + limit

        self.milestones = query[offset:max]

        response = super(MilestoneTableAbstractView, self).dispatch(request, *args, **kwargs)
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
    def dispatch(self, request, *args, **kwargs):
        self.links = [
            {"page": "Bootstrap", "url": reverse("bootstrap")},
            {"page": "Bulma", "url": reverse("bulma")},
            {"page": "GraphiQL", "url": reverse("graphql")},
            {"page": "Swagger API", "url": reverse("api-docs")},
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


class BulmaMilestoneTableView(MilestoneTableAbstractView):
    template_name = "resume/bulma/milestone_table.html"


class BulmaMilestoneDetailView(MilestoneDetailAbstractView):
    template_name = "resume/bulma/milestone_detail.html"
    model = Milestone
    HX_TRIGGER = "openBulmaModal"


class BulmaWorkHistoryView(WorkHistoryAbstractView):
    template_name = "resume/bulma/work_history.html"
