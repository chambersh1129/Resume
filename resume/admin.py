from django.contrib import admin

from .models import Hobby, Milestone, Tag


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "tag", "start_date", "end_date"]

    def tag(self, obj):
        return ", ".join([str(tag) for tag in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
