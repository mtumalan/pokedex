def filter_pokemon_by_type(pokemon_list, pokemon_type):
    '''
    This function filters a list of pokemons by type.
    '''
    return [pokemon for pokemon in pokemon_list if pokemon_type in pokemon['types']]

def filter_pokemon_by_weight(pokemon_list, min_weight, max_weight):
    '''
    This function filters a list of pokemons by weight.
    '''
    return [pokemon for pokemon in pokemon_list if min_weight <= pokemon['weight'] <= max_weight]

def filter_pokemon_by_height(pokemon_list, min_height, max_height):
    '''
    This function filters a list of pokemons by height.
    '''
    return [pokemon for pokemon in pokemon_list if min_height <= pokemon['height'] <= max_height]