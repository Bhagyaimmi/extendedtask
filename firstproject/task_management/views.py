from rest_framework import generics
from .serializers import ProjectSerializer, TaskSerializer
from .models import Project, Task
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from firstapp.views import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



class TaskAssign(APIView):
    def put(self, request, pk, user_id):
        try:
            task = Task.objects.get(pk=pk)
            user = User.objects.get(pk=user_id)
            task.assigned_to = user 
            task.save()
            return Response({'message': 'Task assigned successfully'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserTasksList(APIView):
    def get(self, request, user_id):
        try:
            tasks = Task.objects.filter(assigned_to=user_id)
            task_data = [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
            return Response(task_data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'No tasks assigned to this user'}, status=status.HTTP_404_NOT_FOUND)
        

        









    
