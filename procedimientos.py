import requests
import json

def procedimientos_asteroides(texto, fecha_str, suma_diametros, suma_distancias):
    while fecha <= fin:
        asteroides_detectados = texto["element_count"]
        cantidad_asteroides.append(asteroides_detectados)
        print("El", fecha_str, "se detectaron" ,asteroides_detectados, "elementos")
 
        asteroides = texto["near_earth_objects"][fecha_str]
    
        for ast in asteroides:
            diametro_max_estimados = ast["estimated_diameter"]["meters"]["estimated_diameter_max"]
            suma_diametros = suma_diametros + diametro_max_estimados
        prom_de_diametros_max_estiamados = suma_diametros/asteroides_detectados 
        print("Promedio en metros de diametros máximos estimados:", prom_de_diametros_max_estiamados)
        prom_diametros.append(prom_de_diametros_max_estiamados)
    
 
        for ast in asteroides:
            distancia = ast["close_approach_data"][0]["miss_distance"]["astronomical"]
            suma_distancia = suma_distancia + float(distancia)
        prom_de_distancia = suma_distancia/asteroides_detectados 
        print("Promedio en km de distancia:", prom_de_distancia)
        prom_distancias.append(prom_de_distancia)
 
        fechas.append(fecha_str)
        
        fecha += timedelta(days=1)
        return cantidad_asteroides
        return prom_diametros
        return prom_distancias
        return fechas
        
