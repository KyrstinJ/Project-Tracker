# Generated by Django 4.2 on 2023-04-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_rename_assigne_task_assignee_task_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(),
        ),
    ]
