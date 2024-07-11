from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, ListView

from food.models import Recipe, Ingredient
from .forms import RecipeUpdateForm, IngredientsUpdateForm


# Create your views here.
class RecipeUpdateView(FormView):
    form_class = RecipeUpdateForm
    template_name = 'food/recipe_form.html'

    def form_valid(self, form):
        form.save()


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'


class RecipeListView(ListView):
    model = Recipe


class IngredientCreateView(FormView):
    form_class = IngredientsUpdateForm
    template_name = 'food/ingredient_form.html'

    def get_context_data(self, **kwargs):
        recipe_pk = self.kwargs['pk']
        context = super(IngredientCreateView, self).get_context_data()
        context['recipe'] = get_object_or_404(Recipe, pk=recipe_pk)
        return context

    def form_valid(self, form):
        recipe_pk = self.kwargs['pk']
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        ingredient = Ingredient(recipe=recipe, name=form.cleaned_data['name'], quantity=form.cleaned_data['quantity'])
        ingredient.save()
        if 'add-another' in self.request.POST:
            return redirect(reverse_lazy('Ingredient-create', kwargs={'pk': recipe_pk}))
        return redirect('recipe-detail', pk=recipe_pk)

    # success_url = reverse()


class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'

    # def form_valid(self, form):
    #     # response = super(RecipeCreateView, self).form_valid(form)
    #     # self.object = form.save()
    #     return redirect(reverse_lazy('Ingredient-create', kwargs={'pk': self.object.pk}))

    def get_success_url(self):
        return reverse_lazy('Ingredient-create', kwargs={'pk': self.object.pk})
