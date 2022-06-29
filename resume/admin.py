from django.contrib import admin

from .models import AboutMe, Hobby, Milestone, Tag, WorkHistory


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ["hobby"]


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "tags"]
    list_filter = ["type"]


@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "start_date", "end_date", "total_time"]


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ["full_name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
