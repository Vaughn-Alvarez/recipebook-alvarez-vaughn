from django.db import models

class Recipe(models.Model):

    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=100)
   
class Ingredient(models.Model):

    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=100)

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
    
    
