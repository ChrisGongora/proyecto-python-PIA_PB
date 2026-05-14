import matplotlib.pyplot as plt
def graficas_cantidad_asteroides(fechas, cantidad_asteroides):
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.plot(fechas, cantidad_asteroides, marker = '*', linestyle = ':')
    plt.title("Cantidad de asteroides detectados")
    plt.xlabel("Fechas")
    plt.ylabel("Cantidad")
    plt.show()
def graficas_diametro_asteroides(fechas, prom_diametros):
    plt.plot(fechas, prom_diametros, marker = '*', linestyle = ':')
    plt.title("Diámetro máximo promedio de los asteroides")
    plt.xlabel("Fechas")
    plt.ylabel("Diámetro (metros)")
    plt.show()
def graficas_distancia_asteroides(fechas, prom_distancias):
    plt.plot(fechas, prom_distancias, marker = '*', linestyle = ':')
    plt.title("Distancia promedio de los asteroides")
    plt.xlabel("Fechas")
    plt.ylabel("Distancia (Unidades astronómicas)")
    plt.show()

