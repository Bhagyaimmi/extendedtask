from rest_framework import generics
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from firstapp.views import User

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# class CreateUser(APIView):
#     def post(self, request):
#         try:
#             username = request.data.get('username')
#             password = request.data.get('password')
#             user = User.objects.create_user(username=username, password=password)
            
#             return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# class UserList(APIView):
#     def get(self, request):
#         try:
#             users = User.objects.all()
#             user_list = [{'id': user.id, 'username': user.username} for user in users]
#             return Response(user_list, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        

        









    
