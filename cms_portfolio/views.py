from django.shortcuts import render
import json # for json.dumps
from django.core import serializers
from .models import Project

from django.http import JsonResponse

# Create your views here.


def project_list(request):
    projects = Project.objects.all()
    data = serializers.serialize('json',projects)
    data = json.loads(data)
    return JsonResponse(data,safe=False)

def project_detail(request,pk):
    project = Project.objects.filter(pk=pk)
    data = serializers.serialize('json',project)
    data = json.loads(data)
    return JsonResponse(data,safe=False)
