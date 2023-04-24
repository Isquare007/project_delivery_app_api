"""task views"""
from pd_app.models import Project, Task
from pd_app.serializer import TaskSerializer

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def task_getpost(request, project_id):
    """serves 'GET and 'POST request"""
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id)
        all_tasks = Task.objects.filter(project_id=project)
        serialized = TaskSerializer(all_tasks, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        try:
            project = Project.objects.get(pk=project_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = TaskSerializer(data=request.data)

        if serialized.is_valid():
            serialized.project_id = project
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tasks(request, project_id, task_id):
    """serves all 'GET', 'PUT', 'DELETE' request"""
    try:
        project = Project.objects.get(pk=project_id)
        task = project.tasks.get(pk=task_id)
    except ObjectDoesNotExist:
        return Response({'error': 'Project or task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = TaskSerializer(task)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized = TaskSerializer(task, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
