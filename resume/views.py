from django.urls import reverse
from django.views.generic import TemplateView

from .models import Hobby, Milestone, Profile


class AbstractResumeView(TemplateView):
    curr_framework = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        if profile:
            context["profile"] = profile
            context["milestones"] = Milestone.objects.filter(profile=profile)
            context["hobbies"] = Hobby.objects.filter(profile=profile)
            context["navbar"] = [
                {"page": "Home", "url": reverse("home")},
                {"page": "Bootstrap", "url": reverse("bootstrap")},
                {"page": "Bulma", "url": reverse("bulma")},
            ]

        context["framework"] = self.curr_framework
        return context


class HomePageView(AbstractResumeView):
    template_name = "resume/base.html"


class BootstrapView(AbstractResumeView):
    template_name = "resume/bootstrap/base.html"
    curr_framework = "Bootstrap"


class BulmaView(AbstractResumeView):
    template_name = "resume/bulma/base.html"
    curr_framework = "Bulma"
