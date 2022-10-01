from django.contrib import admin
from cook.models import Recipe, Ingredient, UserIngredient

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(UserIngredient)
