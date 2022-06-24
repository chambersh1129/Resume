from django.views.generic import TemplateView
from django.urls import reverse
from .models import Hobby, Milestone


class AbstractResumeView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["milestones"] = Milestone.objects.all()
        context["hobbies"] = Hobby.objects.all()
        context["navbar"] = [
            {"page": "Home", "url": reverse("home")},
            {"page": "Alpine.js", "url": reverse("alpine")},
            {"page": "Bootstrap", "url": reverse("bootstrap")},
            {"page": "Bulma.js", "url": reverse("bulma")},
            {"page": "TailwindCSS", "url": reverse("tailwind")},
        ]
        return context


class HomePageView(AbstractResumeView):
    template_name = "resume/base.html"


class AlpineView(AbstractResumeView):
    template_name = "resume/alpine.html"


class BootstrapView(AbstractResumeView):
    template_name = "resume/bootstrap.html"


class BulmaView(AbstractResumeView):
    template_name = "resume/bulma.html"


class TailWindView(AbstractResumeView):
    template_name = "resume/tailwind.html"
