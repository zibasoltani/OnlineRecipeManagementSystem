from .models import Recipe, Category
from django import forms


class RecipeUpdateForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Recipe
        fields = '__all__'


# class RecipeDeleteForm(forms.ModelForm):
#     class Meta:
