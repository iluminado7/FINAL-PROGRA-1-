import json
def cargar_ranking(ruta_de_archivo):
    try:
        with open(ruta_de_archivo, "r") as file:
            return json.load(file)
    except:
        # Si el archivo no existe, devuelve un ranking vacio
        return {}

