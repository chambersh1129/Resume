from django.contrib import admin

from .models import Hobby, Milestone, Profile, Tag


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ["title", "profile", "img"]


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ["title", "profile", "type", "tags", "start_date", "end_date"]
    list_filter = ["type", "start_date", "end_date"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["fullname", "email"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
