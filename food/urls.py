from django.contrib import admin
from django.urls import path
from food.views import RecipeCreateView, RecipeDetailView

urlpatterns = [
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/detail/', RecipeDetailView.as_view(), name='recipe-detail')



]