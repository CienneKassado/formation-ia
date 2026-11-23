import requests

def appeler_pokemon(nom):
    reponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nom}")
    
    if reponse.status_code == 200:
        data = reponse.json()
        print(f"Nom : {data['name']}")
        print(f"Poids : {data['weight']}")
        print(f"Taille : {data['height']}")
    elif reponse.status_code == 404:
        print(f"Erreur : '{nom}' n'existe pas dans l'API")
    else:
        print(f"Erreur inattendue : {reponse.status_code}")

appeler_pokemon("pikachu")
print("---")
appeler_pokemon("claudelechat")