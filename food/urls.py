from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/all/', views.RecipeListView.as_view(), name='recipe-all'),
    path('recipe/<int:pk>/detail/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe-edit'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/<int:recipe_id>/ingredient/create/', views.IngredientCreateView.as_view(), name='ingredient-create'),
    path('recipe/<int:recipe_id>/ingredient/<int:pk>/edit/', views.IngredientUpdateView.as_view(), name='ingredient-edit'),
]

# todo: create recipie with adding categories
