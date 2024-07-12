from django.contrib import admin
from .models import Recipe, Ingredient, Category
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Ingredient)