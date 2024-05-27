from django.db import models
from django.contrib.auth.models import User 

# class User(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100) 
#     def __str__(self):
#         return self.username

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='articles',null=True, blank=True )
    def __str__(self):
        return self.title

