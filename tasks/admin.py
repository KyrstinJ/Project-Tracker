from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskItem(admin.ModelAdmin):
    list_display = (
        "name",
        "start_date",
        "due_date",
        "is_completed",
        "project",
        "assignee",
        "id",
    )
