from django.shortcuts import render
from .utils import get_n_cache_pokemon_details, pagination, set_name_backwards
from .filters import filter_pokemon_by_type, filter_pokemon_by_weight, filter_pokemon_by_height


def pokemon_list(request):
    '''
    This function retrieves a list of the first 50 pokemons from PokeAPI and renders it to the user.
    '''
    detailed_pokemons = get_n_cache_pokemon_details() # Get the list of detailed pokemons
    
    page_obj = pagination(detailed_pokemons, request.GET.get('page'), 10) # Set pagination for table
    
    return render(request, 'pokedex/pokemon_list.html', {'page_obj': page_obj}) # Render the list of pokemons to the user
    
    
def pokemon_weight3080(request):
    '''
    This function retrieves a list of the pokemons that weight between 30 and 80 and renders it to the user.
    '''
    detailed_pokemons = get_n_cache_pokemon_details() # Get the list of detailed pokemons
    filtered_pokemons = filter_pokemon_by_weight(detailed_pokemons, 30, 80) # Filter the list of pokemons by weights between 30 and 80
    
    return render(request, 'pokedex/pokemon_weight.html', {'pokemons': filtered_pokemons}) # Render the list of pokemons to the user
    
    
def pokemon_grass(request):
    '''
    This function retrieves a list of the pokemons that are of type grass and renders it to the user.
    '''
    detailed_pokemons = get_n_cache_pokemon_details() # Get the list of detailed pokemons
    filtered_pokemons = filter_pokemon_by_type(detailed_pokemons, 'grass') # Filter the list of pokemons by type
    
    return render(request, 'pokedex/pokemon_grass.html', {'pokemons': filtered_pokemons}) # Render the list of pokemons to the user


def pokemon_fly_height(request):
    '''
    This function retrieves a list of the pokemons that are of type fly, their height is greater than 10 and renders it to the user.
    '''
    detailed_pokemons = get_n_cache_pokemon_details() # Get the list of detailed pokemons
    filtered_pokemons = filter_pokemon_by_type(detailed_pokemons, 'flying') # Filter the list of pokemons by type
    filtered_pokemons = filter_pokemon_by_height(filtered_pokemons, 10, 100) # Filter the list of the previously filtered pokemons by height
    
    return render(request, 'pokedex/pokemon_fly_height.html', {'pokemons': filtered_pokemons}) # Render the list of pokemons to the user


def name_backwards(request):
    '''
    This function retrieves a list of the pokemons and their names backwards and renders it to the user.
    '''
    
    detailed_pokemons = get_n_cache_pokemon_details() # Get the list of detailed pokemons
    backwards_pokemons = set_name_backwards(detailed_pokemons) # Set the names of the pokemons backwards
    
    page_obj = pagination(backwards_pokemons, request.GET.get('page'), 10) # Set pagination for table
    
    return render(request, 'pokedex/pokemon_backwards.html', {'page_obj': page_obj}) # Render the list of pokemons to the user