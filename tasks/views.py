from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.author = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_task(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "show_task": tasks,
    }
    return render(request, "tasks/list.html", context)
