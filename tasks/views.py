from django.shortcuts import render, get_object_or_404, redirect
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
    return render(request, "projects/create.html", context)
