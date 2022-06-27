from django.contrib import admin

from .models import AboutMe, Hobby, JobRole, Milestone, Tag


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ["hobby"]


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "tags", "start_date", "end_date", "total_time"]
    list_filter = ["type", "start_date", "end_date"]


@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "start_date", "end_date", "total_time"]


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ["full_name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
