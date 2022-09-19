from django.contrib import admin
from cook.models import Recipe, Ingredient

admin.site.register(Ingredient)
admin.site.register(Recipe)
