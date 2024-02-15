from django.urls import path

from .views import recipe_list, recipe1, recipe2

urlpatterns = [
    path('list', recipe_list, name='recipe_list'),
    path('1', recipe1, name='1'),
    path('2', recipe1, name='2')
]

app_name = 'recipes'
