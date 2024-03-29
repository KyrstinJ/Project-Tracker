from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(
        null=False,
        blank=False,
    )
    due_date = models.DateTimeField(
        null=False,
        blank=False,
    )
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project", related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        User,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True,
    )
