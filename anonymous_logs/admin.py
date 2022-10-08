from django.contrib import admin

from .models import AnonymousLogs


# Register your models here.
@admin.register(AnonymousLogs)
class AnonymousLogsAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "user_agent", "path"]
    list_filter = ["timestamp", "user_agent", "path"]
    search_fields = ["path", "user_agent"]
