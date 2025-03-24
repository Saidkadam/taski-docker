"""Dogstring."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Dogstring Task."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
