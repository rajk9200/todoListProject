from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.


def task_list(request):
    return render(request,'index.html')

def task_add(request):
    if request.POST:
        task_name =request.POST.get("task_name")
        print(task_name)
        if task_name:
            Task.objects.create(name=task_name)
            return redirect('/')

    return HttpResponse("Added")

def task_delete(request,id=None):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponse("Task Deleted")
    except:
        return HttpResponse("Task Deleted")

def tasks(request):
    tasks =Task.objects.filter().order_by('-id')
    context={
        "tasks":tasks
    }
    return render(request,'task.html',context)

def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")

