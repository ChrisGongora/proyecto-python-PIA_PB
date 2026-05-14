def num_de_asteroides(fecha, fin, texto, cantidad_asteroides):
    asteroides_detectados = texto["element_count"]
    cantidad_asteroides.append(asteroides_detectados)
    return cantidad_asteroides

def diametro_asteroides(texto, fecha_str, prom_diametros, suma_diametros):
    asteroides = texto["near_earth_objects"][fecha_str]
    asteroides_detectados = texto["element_count"]
    for ast in asteroides:
        diametro_max_estimados = ast["estimated_diameter"]["meters"]["estimated_diameter_max"]
        suma_diametros = suma_diametros + diametro_max_estimados
    prom_de_diametros_max_estiamados = suma_diametros/asteroides_detectados 
    prom_diametros.append(prom_de_diametros_max_estiamados)
    return prom_diametros
    
def distancia_asteroides(texto, fecha_str, prom_distancias, suma_distancia):
     asteroides = texto["near_earth_objects"][fecha_str]
     asteroides_detectados = texto["element_count"]
     for ast in asteroides:
         distancia = ast["close_approach_data"][0]["miss_distance"]["astronomical"]
         suma_distancia = suma_distancia + float(distancia)
     prom_de_distancia = suma_distancia/asteroides_detectados
     prom_distancias.append(prom_de_distancia)
     return prom_distancias

def fechas_asteroides(fechas, fecha_str):
    fechas.append(fecha_str)
    return fechas
        
