from rest_framework import serializers
from .models import User, Product, Article
from task_management.serializers import TaskSerializer,ProjectSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'author']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'product']

class UserSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'products', 'articles','password', 'tasks','projects']
        
    def create(self, validated_data):
         return User.objects.create(**validated_data)
  
       