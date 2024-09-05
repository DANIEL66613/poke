import requests

def get_request(nome_pokemon):
    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"
    #url_evolution = f"https://pokeapi.co/api/v2/evolution-chain/{id}/"
    url_games = f"https://pokeapi.co/api/v2/generation/{nome_pokemon.lower()}/"

    dados_pokemon = requests.get(url_pokemon)
    dados = dados_pokemon.json()

    #evolution_pokemon = requests.get(url_evolution)
    #dados_evolution = evolution_pokemon.json()

    games_pokemon = requests.get(url_games)
    dados_games = games_pokemon.json()

    return dados, dados_games

dados_da_requisicao = get_request("pikachu")


nome_pokemon = dados_da_requisicao['name']
tipos = [tipo['type']['name'] for tipo in dados_da_requisicao['types']]
movimentos = [move['move']['name'] for move in dados_da_requisicao['moves']]

print(f"Nome: {nome_pokemon.capitalize()}")
print("Tipos:", ", ".join(tipos).capitalize())
print("Movimentos:", ", ".join(movimentos).capitalize())

