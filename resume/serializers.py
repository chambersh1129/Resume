from rest_framework import serializers

from .models import AboutMe, Hobby, Milestone, Tag, WorkHistory


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ["full_name", "title", "email", "github", "linkedin"]


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ["id", "hobby", "description"]


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = ["id", "company", "title", "description", "start_date", "end_date", "total_time"]


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ["id", "name", "description", "type", "tags"]


class MilestoneTypeSerializer(serializers.BaseSerializer):
    type = serializers.CharField(max_length=Milestone.type.field.max_length)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
