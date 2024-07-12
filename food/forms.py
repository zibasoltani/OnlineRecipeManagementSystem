from .models import Recipe, Category, Ingredient
from django import forms


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'description': forms.TextInput(attrs={'readonly': 'readonly'}),
            'categories': forms.TextInput(attrs={'readonly': 'readonly'}),
            'instructions': forms.TextInput(attrs={'readonly': 'readonly'}),
            'cooking_time': forms.TextInput(attrs={'readonly': 'readonly'}),
            'difficulty_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'preparation_time': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        # widgets = {
        #     'title': forms.TextInput(attrs={'disabled': True}),
        #     'description': forms.TextInput(attrs={'disabled': True}),
        #     'categories': forms.TextInput(attrs={'disabled': True}),
        #     'instructions': forms.TextInput(attrs={'disabled': True}),
        #     'cooking_time': forms.TextInput(attrs={'disabled': True}),
        #     'difficulty_level': forms.TextInput(attrs={'disabled': True}),
        #     'preparation_time': forms.TextInput(attrs={'disabled': True}),
        # }
        # fields = ['title']
        # widgets = {'title': forms.TextInput(attrs={'disabled': True})}
