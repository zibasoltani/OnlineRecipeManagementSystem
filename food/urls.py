from django.contrib import admin
from django.urls import path
from food.views import RecipeCreateView, RecipeDetailView, IngredientCreateView

urlpatterns = [
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/detail/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/create_ingredient', IngredientCreateView.as_view(), name='Ingredient-create')



]