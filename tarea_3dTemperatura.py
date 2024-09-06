# Datos de temperaturas esta compuesta 
# (Matriz 3D: Ciudades, Semanas, Días de la semana)

temperaturas = [
    [   # Ciudad 1
        [78, 80, 82, 60, 85, 88, 92],  # Semana 1
        [76, 79, 83, 81, 87, 89, 93],  # Semana 2
        [77, 81, 85, 82, 88, 91, 95],  # Semana 3
        [75, 78, 80, 79, 84, 87, 91]   # Semana 4
    ],
    [   # Ciudad 2
        [62, 64, 68, 70, 73, 75, 79],  # Semana 1
        [63, 66, 70, 80, 75, 77, 81],  # Semana 2
        [61, 65, 68, 70, 72, 76, 80],  # Semana 3
        [64, 67, 69, 71, 74, 77, 80]   # Semana 4
    ],
    [   # Ciudad 3
        [90, 94, 94, 91, 88, 85, 82],  # Semana 1
        [89, 91, 93, 90, 87, 84, 81],  # Semana 2
        [91, 93, 90, 92, 89, 86, 83],  # Semana 3
        [88, 90, 92, 89, 86, 83, 80]   # Semana 4
    ]
]

# Función para calcular el promedio de una semana
def calcular_promedio(temperaturas_semana):
    return sum(temperaturas_semana) / len(temperaturas_semana)

# Función para mostrar los promedios por ciudad y semana
def mostrar_promedios(temperaturas):
    for indice_ciudad, ciudad in enumerate(temperaturas):
        print(f"\nCiudad {indice_ciudad + 1}:")
        for indice_semana, semana in enumerate(ciudad):
            promedio = calcular_promedio(semana)
            print(f"  Semana {indice_semana + 1}: Promedio = {promedio:.2f}")

# Llamada a la función para mostrar los resultados
mostrar_promedios(temperaturas)

