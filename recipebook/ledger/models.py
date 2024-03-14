from django.db import models
from django.urls import reverse


class Recipe(models.Model):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])


class Ingredient(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[self.pk])


class RecipeIngredient(models.Model):

    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="ingredients"
    )
    ingredient = models.ForeignKey(
        "Ingredient",
        on_delete=models.CASCADE,
        related_name="recipe"
    )
