from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
from accounts.models import Profile
from django.contrib.auth.models import User


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]
    fieldsets = [
        ('Details', {
            'fields': [
                'name',
                'author'
            ]
        })
    ]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
