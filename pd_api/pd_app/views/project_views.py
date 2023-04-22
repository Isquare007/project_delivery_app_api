"""project views"""
from pd_app.models import Project
from pd_app.serializer import ProjectSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

@api_view(['GET', 'POST'])
def project_getpost(request):
    """serves 'GET and 'POST request"""
    if request.method == 'GET':
        projects = Project.objects.all()
        serialized = ProjectSerializer(projects, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        serialized = ProjectSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def projects(request, id):
    """serves all 'GET', 'PUT', 'DELETE' request"""
    try:
        project = Project.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = ProjectSerializer(project)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized = ProjectSerializer(project, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
