from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Title:{self.title}'


class Recipe(models.Model):

    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.TextField(max_length=500)
    description = models.TextField(max_length=3000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    choices = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f'Title:{self.title}'
