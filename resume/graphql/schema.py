import graphene
from graphene_django.filter import DjangoFilterConnectionField

from resume.models import AboutMe

from .types import AboutMeType, HobbyNode, MilestoneNode, TagNode, WorkHistoryNode


class Query(graphene.ObjectType):
    about_me = graphene.Field(AboutMeType)
    hobbies = DjangoFilterConnectionField(HobbyNode)
    milestones = DjangoFilterConnectionField(MilestoneNode)
    tags = DjangoFilterConnectionField(TagNode)
    work_history = DjangoFilterConnectionField(WorkHistoryNode)

    def resolve_about_me(root, info):
        return AboutMe.objects.first()


schema = graphene.Schema(query=Query)
