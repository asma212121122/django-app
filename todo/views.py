from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title :
            Task.objects.create(title=title)
    
    tasks = Task.objects.all().order_by('-created_at')
    return render(request , "todo/task_list.html", {"tasks": tasks})