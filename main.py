from datetime import datetime, timedelta
from descarga import informacion_por_fechas
from procedimientos import num_de_asteroides, diametro_asteroides, distancia_asteroides, fechas_asteroides
from graficas import graficas_cantidad_asteroides, graficas_diametro_asteroides, graficas_distancia_asteroides

inicio = datetime(2025, 1, 1)
fin = datetime(2025, 1, 19)
fecha = inicio

suma_diametros = 0
suma_distancia = 0
cantidad_asteroides = []
prom_diametros = []
prom_distancias = []
fechas = []

while fecha <= fin:
    fecha_str = fecha.strftime("%Y-%m-%d")
    texto = informacion_por_fechas(fecha_str)
    cantidad_asteroides = num_de_asteroides(fecha, fin, texto, cantidad_asteroides)
    prom_diametros = diametro_asteroides(texto, fecha_str, prom_diametros, suma_diametros)
    prom_distancias = distancia_asteroides(texto, fecha_str, prom_distancias, suma_distancia)
    fechas = fechas_asteroides(fechas, fecha_str)
    fecha += timedelta(days=1)
    
graficas_cantidad_asteroides(fechas, cantidad_asteroides)
graficas_diametro_asteroides(fechas, prom_diametros)
graficas_distancia_asteroides(fechas, prom_distancias)
