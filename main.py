import requests
import json
from datetime import datetime, timedelta
from descarga import informacion_por_fechas
from procedimientos import procedimientos_asteroides
from graficas import graficas_asteroides


inicio = datetime(2025, 12, 20)
fin = datetime(2025, 12, 20)
fecha = inicio

suma_diametros = 0
suma_distancia = 0
cantidad_asteroides = []
prom_diametros = []
prom_distancias = []
fechas = []

def informacion_por_fechas(inicio, fin):
    def procedimientos_asteroides():
        def graficas_asteroides():
