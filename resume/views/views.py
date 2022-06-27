from django.urls import reverse
from django.views.generic import TemplateView

from resume.models import AboutMe


class AboutAbstractView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = AboutMe.objects.first()
        return context


class URLAbstractView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["links"] = [
            {"framework": "Home", "url": reverse("home")},
            {"framework": "Bootstrap", "url": reverse("bootstrap")},
            {"framework": "Bulma", "url": reverse("bulma")},
        ]
        return context


class HomePageView(AboutAbstractView, URLAbstractView):
    template_name = "resume/home.html"


class BootstrapView(AboutAbstractView, URLAbstractView):
    template_name = "resume/bootstrap/base.html"
    curr_framework = "Bootstrap"


class BulmaView(AboutAbstractView, URLAbstractView):
    template_name = "resume/bulma/base.html"
    curr_framework = "Bulma"
