from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Title:{self.title}'


class UserIngredient(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    elem = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Продукт:{self.elem}'

class Recipe(models.Model):

    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.TextField(max_length=500)
    description = models.TextField(max_length=3000)
    user_ingrs = models.ForeignKey(UserIngredient, on_delete=models.CASCADE, blank=True, null=True) 
    
    def __str__(self):
        return f'Title:{self.title}'
