import requests
import json

def informacion_por_fechas(fecha_str):
    url= "https://api.nasa.gov/neo/rest/v1/feed?start_date="+fecha_str+"&end_date="+fecha_str+"&api_key=qJz6XXC44eUmowIdeDx1pYomWodqRJCWzRa1ynXF"
    info = requests.get(url)
    texto = json.loads(info.text)
    return texto
