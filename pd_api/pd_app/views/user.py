"""Users views"""
from pd_app.models import Project, User
from pd_app.serializer import UserSerializer

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def user_getpost(request, project_id):
    """serves 'GET and 'POST request"""
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id)
        # all_users = User.objects.filter(project_id=project)
        all_users = project.users.all()
        serialized = UserSerializer(all_users, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        try:
            project = Project.objects.get(pk=project_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = UserSerializer(data=request.data)

        if serialized.is_valid():
            serialized.project_id = project
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def users(request, project_id, user_id):
    """serves all 'GET', 'PUT', 'DELETE' request"""
    try:
        project = Project.objects.get(pk=project_id)
        user = project.users.get(pk=user_id)
    except ObjectDoesNotExist:
        return Response({'error': 'Project or task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = UserSerializer(user)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized = UserSerializer(user, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def list_users(request, user_id=0):
    """list all the users in the database"""
    if user_id != 0:
        try:
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = UserSerializer(user)
        return Response(serialized.data)

    users = User.objects.all()
    serialized = UserSerializer(users, many=True)
    return Response(serialized.data)
