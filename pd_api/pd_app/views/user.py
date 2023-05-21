from pd_app.models import Project, CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from pd_app.serializer import CustomUserSerializer


@api_view(['GET', 'POST'])
def user_getpost(request, project_id):
    """Serves 'GET' and 'POST' requests for users"""
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id)
        all_users = project.user_assigned.all()
        serialized = CustomUserSerializer(all_users, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        try:
            project = Project.objects.get(pk=project_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        user = CustomUser.objects.create_user(username=request.data['username'], password=request.data['password'])
        project.user_assigned.add(user)

        return Response({'message': 'User created and assigned to the project'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def users(request, project_id, user_id):
    """Serves 'GET', 'PUT', 'DELETE' requests for a user"""
    try:
        project = Project.objects.get(pk=project_id)
        user = project.user_assigned.get(pk=user_id)
    except ObjectDoesNotExist:
        return Response({'error': 'Project or user not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = CustomUserSerializer(user)
        return Response(serialized.data)

    elif request.method == 'PUT':
        serialized = CustomUserSerializer(user, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.user_assigned.remove(user)
        return Response({'message': 'User removed from the project'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def list_users(request, user_id=0):
    """Lists all the users in the database"""
    if user_id != 0:
        try:
            user = CustomUser.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = CustomUserSerializer(user)
        return Response(serialized.data)

    users = CustomUser.objects.all()
    serialized = CustomUserSerializer(users, many=True)
    return Response(serialized.data)












# """Users views"""
# from pd_app.models import Project, User
# from pd_app.serializer import UserSerializer

# from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.

# @api_view(['GET', 'POST'])
# def user_getpost(request, project_id):
#     """serves 'GET and 'POST request"""
#     if request.method == 'GET':
#         project = get_object_or_404(Project, pk=project_id)
#         # all_users = User.objects.filter(project_id=project)
#         all_users = project.users.all()
#         serialized = UserSerializer(all_users, many=True)
#         return Response(serialized.data)

#     if request.method == 'POST':
#         try:
#             project = Project.objects.get(pk=project_id)
#         except ObjectDoesNotExist:
#             return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = UserSerializer(data=request.data)

#         if serialized.is_valid():
#             serialized.project_id = project
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def users(request, project_id, user_id):
#     """serves all 'GET', 'PUT', 'DELETE' request"""
#     try:
#         project = Project.objects.get(pk=project_id)
#         user = project.users.get(pk=user_id)
#     except ObjectDoesNotExist:
#         return Response({'error': 'Project or task not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serialized = UserSerializer(user)
#         return Response(serialized.data)

#     elif request.method == 'PUT':
#         serialized = UserSerializer(user, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET'])
# def list_users(request, user_id=0):
#     """list all the users in the database"""
#     if user_id != 0:
#         try:
#             user = User.objects.get(pk=user_id)
#         except ObjectDoesNotExist:
#             return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = UserSerializer(user)
#         return Response(serialized.data)

#     users = User.objects.all()
#     serialized = UserSerializer(users, many=True)
#     return Response(serialized.data)
