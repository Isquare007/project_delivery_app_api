"""Milestones views"""
from pd_app.models import Project, Milestone
from pd_app.serializer import MilestoneSerializer

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def milestone_getpost(request, project_id):
    """serves 'GET and 'POST request"""
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id)
        # all_users = User.objects.filter(project_id=project)
        all_milestones = project.milestone.all()
        serialized = MilestoneSerializer(all_milestones, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        try:
            project = Project.objects.get(pk=project_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = MilestoneSerializer(data=request.data)

        if serialized.is_valid():
            serialized.project_id = project
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def milestones(request, project_id, milestone_id):
    """serves all 'GET', 'PUT', 'DELETE' request"""
    try:
        project = Project.objects.get(pk=project_id)
        milestone = project.milestone.get(pk=milestone_id)
    except ObjectDoesNotExist:
        return Response({'error': 'Project or task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = MilestoneSerializer(milestone)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized = MilestoneSerializer(milestone, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        milestone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def list_milestones(request, milestone_id=0):
    """list all the users in the database"""
    if milestone_id != 0:
        try:
            milestone = Milestone.objects.get(pk=milestone_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = MilestoneSerializer(milestone)
        return Response(serialized.data)
    
    milestones = Milestone.objects.all()
    serialized = MilestoneSerializer(milestones, many=True)
    return Response(serialized.data)
