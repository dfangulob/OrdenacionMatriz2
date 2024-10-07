# Escritura de Archivo de Texto
def escribir_notas(notas, archivo='my_notes.txt'):
    file = open(archivo, 'w')
    for nota in notas:
        file.write(nota + "\n")
    file.close()


# Lectura de Archivo de Texto
def leer_notas(archivo='my_notes.txt'):
    try:
        file = open(archivo, 'r')
        notas = []
        linea = file.readline()
        while linea:
            notas.append(linea.strip())
            linea = file.readline()
        file.close()
        return notas
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return []


# Programa principal
notas = [
    "Nota 1: Voy a realizar la tarea.",
    "Nota 2: Revisar el proyecto de Python.",
    "Nota 3: subir el archivo",
]

escribir_notas(notas)

notas_leidas = leer_notas()
for i, nota in enumerate(notas_leidas, start=1):
    print(f"Nota {i}: {nota}")