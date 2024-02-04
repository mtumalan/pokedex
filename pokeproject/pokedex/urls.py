from django.urls import path
from .views import pokemon_list, pokemon_grass, pokemon_fly_height, pokemon_weight3080, name_backwards

urlpatterns = [
    path('pokemons/', pokemon_list, name='pokemon_list'),
    path('pokemons/weight/', pokemon_weight3080, name='pokemon_weight3080'),
    path('pokemons/grass/', pokemon_grass, name='pokemon_grass'),
    path('pokemons/fly-height/', pokemon_fly_height, name='pokemon_fly_height'),
    path('pokemons/backwards/', name_backwards, name='name_backwards'),
]