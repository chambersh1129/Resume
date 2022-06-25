from django.contrib import admin

from .models import Hobby, Milestone, Profile, Tag


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ["profile", "title", "img"]


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ["profile", "title", "type", "tag", "start_date", "end_date"]
    list_filter = ["type", "start_date", "end_date"]

    def tag(self, obj):
        return ", ".join([str(tag) for tag in obj.tags.all()])


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["fullname", "email"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
