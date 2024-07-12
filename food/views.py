from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, DetailView, ListView, UpdateView, DeleteView

from food.models import Recipe, Ingredient
from .forms import RecipeUpdateForm, IngredientsUpdateForm, RecipeDeleteForm


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'food/ingredient_edit_form.html'
    fields = ['name', 'quantity']

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.kwargs.get('recipe_id')})

    def get_context_data(self, **kwargs):
        context = super(IngredientUpdateView, self).get_context_data()
        context['recipe'] = self.object.recipe
        return context


class RecipeUpdateView(FormView):
    form_class = RecipeUpdateForm
    template_name = 'food/recipe_edit_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdateView, self).get_context_data(**kwargs)
        recipe_to_edit = Recipe.objects.get(id=self.kwargs.get('pk'))
        context['form'] = self.form_class(instance=recipe_to_edit)
        context['ingredients'] = recipe_to_edit.ingredients.all()
        return context

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        recipe_to_edit = Recipe.objects.get(id=self.kwargs.get('pk'))
        form = form_class(self.request.POST, instance=recipe_to_edit)
        return form

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'


class RecipeListView(ListView):
    model = Recipe


class IngredientCreateView(FormView):
    form_class = IngredientsUpdateForm
    template_name = 'food/ingredient_creation_form.html'

    def get_context_data(self, **kwargs):
        recipe_pk = self.kwargs['recipe_id']
        context = super(IngredientCreateView, self).get_context_data()
        context['recipe'] = get_object_or_404(Recipe, pk=recipe_pk)
        return context

    def form_valid(self, form):
        recipe_pk = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        ingredient = Ingredient(recipe=recipe, name=form.cleaned_data['name'], quantity=form.cleaned_data['quantity'])
        ingredient.save()
        if 'add-another' in self.request.POST:
            return redirect(reverse_lazy('ingredient-create', kwargs={'recipe_id': recipe_pk}))
        return redirect('recipe-detail', pk=recipe_pk)


class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'food/recipe_creation_form.html'

    def get_success_url(self):
        return reverse_lazy('ingredient-create', kwargs={'recipe_id': self.object.pk})


# class RecipeDeleteView(DeleteView):
#     model = Recipe
#     success_url = reverse_lazy('recipe-all')
#     template_name = 'food/recipe_deletion_form.html'


class RecipeDeleteView(FormView):
    form_class = RecipeDeleteForm
    template_name = 'food/recipe_deletion_form.html'
    success_url = reverse_lazy('recipe-all')

    def get_context_data(self, **kwargs):
        context = super(RecipeDeleteView, self).get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        context['form'] = self.form_class(instance=context['recipe'])
        return context

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        recipe.delete()
        print('*' * 50)
        return super(RecipeDeleteView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(RecipeDeleteView, self).form_invalid(form)



# class RecipeDeleteForm(forms.Form):
#     confirm_delete = forms.BooleanField(label="are you sure you want to delete this recipe?")
#
# class RecipeDeleteView(FormView, LoginRequiredMixin):
#     model = Recipe
#
#     template_name = 'recipe_delete.html'
#     form_class = RecipeDeleteForm
#     success_url = reverse_lazy("recipe:list")
#     login_url = reverse_lazy("login")
#     pk_url_kwarg = 'id'
#
#     def form_valid(self, form):
#         pk = self.kwargs.get("id")
#         recipe = get_object_or_404(Recipe, pk=pk)
#         recipe.delete()
#         return super().form_valid(form)
