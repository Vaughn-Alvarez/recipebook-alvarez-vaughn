from django.db import models
from django.urls import reverse


class Recipe(models.Model):

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])

    name = models.CharField(max_length=100)


class Ingredient(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])


class RecipeIngredient(models.Model):

    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="ingredient"
    )
    ingredient = models.ForeignKey(
        "Ingredient",
        on_delete=models.CASCADE,
        related_name="recipe"
    )
