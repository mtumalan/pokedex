import requests
from django.core.cache import cache
from django.core.paginator import Paginator
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_pokemon_details(url):
    '''
    This function retrieves the detailed information of a pokemon from PokeAPI.
    '''
    response = requests.get(url) # Get the detailed information of the pokemon
    if response.status_code == 200:
        pokemon_data = response.json()
        return { # Return the detailed information of the pokemon
            'id': pokemon_data['id'],
            'name': pokemon_data['name'],
            'types': [t['type']['name'] for t in pokemon_data['types']], # Iterate over the types of the pokemons that are received
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight']
        }

def get_n_cache_pokemon_details():
    """
    This function retrieves a list of the first 50 pokemons from PokeAPI and caches it.
    """
    cached_pokemons = cache.get('detailed_pokemons')  # Try to get the list of detailed pokemons from the cache
    
    if cached_pokemons is None:
        url = 'https://pokeapi.co/api/v2/pokemon?limit=50'
        response = requests.get(url)
        pokemons = response.json()['results'] if response.status_code == 200 else []  # This list gets name and url of each pokemon
        
        # Use ThreadPoolExecutor to fetch details concurrently
        with ThreadPoolExecutor(max_workers=8) as executor: # Use 8 threads to fetch the details of the pokemons, adjust according to CPU thread count
            future_to_pokemon = {executor.submit(fetch_pokemon_details, pokemon['url']): pokemon for pokemon in pokemons} # Create a dictionary with the future objects
            detailed_pokemons = [] # Create an empty list to store the detailed pokemons
            for future in as_completed(future_to_pokemon): # Iterate over the future objects
                detailed_pokemons.append(future.result()) # Append the detailed information of the pokemon to the list
        
        detailed_pokemons.sort(key=lambda x: x['id'])  # Sort the list of detailed pokemons by id
        cache.set('detailed_pokemons', detailed_pokemons, 3600)  # Save the list of detailed pokemons in the cache for 1 hour
    else:
        detailed_pokemons = cached_pokemons  # If the list of detailed pokemons is in the cache, use it
    
    return detailed_pokemons


def pagination(detailed_pokemons, page_number, items_per_page):
    '''
    This function returns a paginator object with the pokemons.
    '''
    paginator = Paginator(detailed_pokemons, items_per_page) # Create a paginator with 10 pokemons per page
    page_obj = paginator.get_page(page_number) # Get the page object
    return page_obj

def set_name_backwards(detailed_pokemons):
    '''
    This function returns a list with id, name and name backwards of each pokemon.
    '''
    return [{'id': pokemon['id'], 'name': pokemon['name'], 'backwards_name': pokemon['name'][::-1]} for pokemon in detailed_pokemons]
    