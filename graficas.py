
def graficas_asteroides(fechas, cantidad_asteroides, prom_diametros, prom_distancias):
    plt.plot(fechas, cantidad_asteroides, marker = 'P', linestyle = 'dashdot')
    plt.show()
 
    plt.plot(fechas, prom_diametros, marker = 'P', linestyle = 'dashdot')
    plt.show()
 
    plt.plot(fechas, prom_distancias, marker = 'P', linestyle = 'dashdot')
    plt.show()

    
