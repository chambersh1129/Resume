import graphene
from graphene_django import DjangoObjectType

from resume.models import AboutMe, Hobby, Milestone, Tag, WorkHistory

from .filters import HobbyFilter, MilestoneFilter, TagFilter, WorkHistoryFilter


class AboutMeType(DjangoObjectType):
    """
    Get information about me, including contact information
    """

    full_name = graphene.String(description="My Full Name")
    title = graphene.String(description="My Current Job Title")
    email = graphene.String(description="My Email Address")
    github = graphene.String(description="My GitHub Profile")
    linkedin = graphene.String(description="My LinkedIn Profile")
    resume = graphene.String(description="Link to Download My Resume")

    class Meta:
        model = AboutMe
        fields = ("id", "email", "github", "linkedin", "resume")

    def resolve_full_name(self, info):
        return self.full_name

    def resolve_title(self, info):
        return self.title


class HobbyNode(DjangoObjectType):
    """
    What I like to do when I'm not working
    """

    hobby = graphene.String(description="The name of the Hobbby")
    description = graphene.String(description="The description of the Hobby")

    class Meta:
        model = Hobby
        fields = ("id", "hobby", "description")
        interfaces = (graphene.relay.Node,)
        filterset_class = HobbyFilter


class MilestoneNode(DjangoObjectType):
    """
    What I consider my major milestones.  Includes projects, certifications, eduction, or anything else I consider
    an accomplishment
    """

    name = graphene.String(description="The name of the Milestone")
    description = graphene.String(description="The description of the Milestone")

    class Meta:
        model = Milestone
        interfaces = (graphene.relay.Node,)
        filterset_class = MilestoneFilter


class TagNode(DjangoObjectType):
    """
    Retrieve the list of Milestone tags
    """

    tag = graphene.String(description="The name of the tag")

    class Meta:
        model = Tag
        fields = ("id", "tag")
        interfaces = (graphene.relay.Node,)
        filterset_class = TagFilter


class WorkHistoryNode(DjangoObjectType):
    """
    My work history, including my current position (if I'm still employeed)
    """

    company = graphene.String(description="The name of the company")
    title = graphene.String(description="The job title")
    description = graphene.String(description="The job description")
    start_date = graphene.Date(description="The date I started")
    end_date = graphene.Date(description="The date I ended")
    total_time = graphene.String(description="The time spent in the role")

    class Meta:
        model = WorkHistory
        fields = ("id", "company", "title", "description", "start_date", "end_date", "total_time")
        interfaces = (graphene.relay.Node,)
        filterset_class = WorkHistoryFilter

    def resolve_total_time(self, info):
        return self.total_time
