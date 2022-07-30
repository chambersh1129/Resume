from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from resume.models import AboutMe, Hobby, Milestone, Tag, WorkHistory

from .filters import MilestoneFilterSet, TagFilterSet, WorkHistoryFilterSet
from .serializers import AboutMeSerializer, HobbySerializer, MilestoneSerializer, TagSerializer, WorkHistorySerializer


class ListViewSet(GenericViewSet, ListModelMixin):
    pass


class AboutMeViewSet(GenericAPIView):
    """
    Get information about me, including contact information
    """

    serializer_class = AboutMeSerializer
    pagination_class = None

    def get(self, request, format=None):
        about = AboutMe.objects.first()
        serialized_data = AboutMeSerializer(about)
        return Response(serialized_data.data)


class HobbyAPIViewSet(ListViewSet):
    """
    What I like to do when I'm not working
    """

    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer


class MilestoneAPIViewSet(ListViewSet):
    """
    What I consider my major milestones.  Includes projects, certifications, eduction, or anything else I consider
    an accomplishment
    """

    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    filter_backends = [MilestoneFilterSet]


class TagAPIViewSet(ListViewSet):
    """
    Retrieve the list of Milestone tags
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [TagFilterSet]


class WorkHistoryAPIViewSet(ListViewSet):
    """
    My work history, including my current position (if I'm still employeed)
    """

    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    filter_backends = [WorkHistoryFilterSet]
