import requests
import json

import requests

def obtener_datos():
    """Descarga y retorna los datos JSON de la API."""
    url = "https://api.nasa.gov/neo/rest/v1/feed?&api_key=qJz6XXC44eUmowIdeDx1pYomWodqRJCWzRa1ynXF"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
