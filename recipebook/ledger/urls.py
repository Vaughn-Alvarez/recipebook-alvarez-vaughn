from django.urls import path

from .views import recipe_list, recipe_1, recipe_2

urlpatterns = [
    path('list', recipe_list, name='recipe_list'),
    path('1', recipe_1, name='1'),
    path('2', recipe_2, name='2')
]

app_name = 'recipes'
