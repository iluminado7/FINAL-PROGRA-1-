import json
def guardar_ranking(ranking, ruta_de_ranking):
    with open(ruta_de_ranking, "w") as file:
        json.dump(ranking, file, indent=4)