from django.shortcuts import render
from django.views.generic import CreateView, FormView, DetailView

from food.models import Recipe
from .forms import RecipeUpdateForm


# Create your views here.
class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'


class RecipeUpdateView(FormView):
    form_class = RecipeUpdateForm
    template_name = 'food/recipe_form.html'

    def form_valid(self, form):
        form.save()


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
