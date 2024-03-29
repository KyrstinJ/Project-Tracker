from django.urls import path
from tasks.views import create_task, show_task


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_task, name="show_my_tasks"),
]
