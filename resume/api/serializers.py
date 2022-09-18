from rest_framework import serializers

from resume.models import AboutMe, Hobby, Milestone, Tag, WorkHistory


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ["full_name", "title", "email", "github", "linkedin", "resume"]


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ["id", "hobby", "description"]


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ["id", "name", "description", "type", "tags"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "tag"]


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = ["id", "company", "title", "description", "start_date", "end_date", "total_time"]
