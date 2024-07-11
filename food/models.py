from django.db import models
from datetime import timedelta

from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    class DifficultyLevel(models.IntegerChoices):
        EASY = 1, "Easy"
        MEDIUM = 2, "Medium"
        HARD = 3, "Hard"

    title = models.CharField(max_length=50)
    description = models.TextField()
    preparation_time = models.DurationField(default=timedelta(minutes=42))
    cooking_time = models.DurationField(default=timedelta(minutes=42))
    instructions = models.TextField()
    difficulty_level = models.IntegerField(choices=DifficultyLevel.choices, default=DifficultyLevel.EASY)

    # def get_absolute_url(self):
    #     return reverse('recipe-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    recipes = models.ManyToManyField(Recipe, related_name="categories")


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
