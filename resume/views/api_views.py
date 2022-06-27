from django.views.generic import TemplateView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from resume.models import AboutMe, Hobby, JobRole, Milestone
from resume.serializers import AboutMeSerializer, HobbySerializer, JobRoleSerializer, MilestoneSerializer


class ListViewSet(GenericViewSet, ListModelMixin):
    pass


class AboutMeViewSet(ListViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class HobbyAPIViewSet(ListViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer


class JobRoleViewSet(ListViewSet):
    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer


class MilestoneAPIViewSet(ListViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer


class SwaggerView(TemplateView):
    template_name = "resume/swagger.html"
    extra_context = {"schema_url": "openapi-schema"}
