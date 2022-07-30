import graphene
from graphene_django import DjangoObjectType

from resume.models import AboutMe, Hobby, Milestone, Tag, WorkHistory

from .filters import HobbyFilter, MilestoneFilter, TagFilter, WorkHistoryFilter


class AboutMeType(DjangoObjectType):
    """
    Get information about me, including contact information
    """

    full_name = graphene.String()
    title = graphene.String()

    class Meta:
        model = AboutMe
        fields = ("id", "email", "github", "linkedin")

    def resolve_full_name(self, info):
        return self.full_name

    def resolve_title(self, info):
        return self.title


class HobbyNode(DjangoObjectType):
    """
    What I like to do when I'm not working
    """

    class Meta:
        model = Hobby
        interfaces = (graphene.relay.Node,)
        filterset_class = HobbyFilter


class MilestoneNode(DjangoObjectType):
    """
    What I consider my major milestones.  Includes projects, certifications, eduction, or anything else I consider
    an accomplishment
    """

    class Meta:
        model = Milestone
        interfaces = (graphene.relay.Node,)
        filterset_class = MilestoneFilter


class TagNode(DjangoObjectType):
    """
    Retrieve the list of Milestone tags
    """

    class Meta:
        model = Tag
        interfaces = (graphene.relay.Node,)
        filterset_class = TagFilter


class WorkHistoryNode(DjangoObjectType):
    """
    My work history, including my current position (if I'm still employeed)
    """

    total_time = graphene.String()

    class Meta:
        model = WorkHistory
        interfaces = (graphene.relay.Node,)
        filterset_class = WorkHistoryFilter

    def resolve_total_time(self, info):
        return self.total_time
