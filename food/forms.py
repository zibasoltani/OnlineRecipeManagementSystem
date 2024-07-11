from .models import Recipe, Category, Ingredient
from django import forms


class RecipeUpdateForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Recipe
        fields = '__all__'


# class RecipeDeleteForm(forms.ModelForm):
#     class Meta:

class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']
