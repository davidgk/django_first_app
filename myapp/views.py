from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from myapp.models import Project, Task, MyEncoder
import json


def index(request):
    title='Django Course!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, name = "world"):
    return HttpResponse(f'<h1>hello {name}</h1>')

def about(request):
    return render(request, 'about.html',{
        'username' : 'davidgk'
    })

def projects(request):
    try:
        projects = list(Project.objects.values())
        return JsonResponse(projects, safe=False)
    except:
        return JsonResponse([])


def project_tasks(request, id_project):
    try:
        project = Project.objects.get(id=id_project)
        tasks = list(Task.objects.filter(project=project).values())
        return JsonResponse(tasks, safe=False)
    except:
        return JsonResponse([])

def task_by_id(request, id_task):
    task = get_object_or_404(Task, id=id_task)
    # a_task_ser = serializers.serialize('json', [task])
    a_task_ser = model_to_dict(task)
    return JsonResponse(json.dumps(a_task_ser), safe=False)


