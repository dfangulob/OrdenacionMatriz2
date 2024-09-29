# Creando  un diccionario llamado 'informacion_personal' con claves nombre
#edad ciudad
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder  y modificar valores al valor asociado con la clave "ciudad" y modificarl
informacion_personal["ciudad"] = "Ibarra"  # Cambiamos la ciudad a Ibarra

# Agregar una nueva clave-valor al diccionario (aunque ya existe la clave "profesion", asumimos que el objetivo es mantenerla)
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizamos la profesión

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"  # Si no existe, se agrega el número ficticio

# Eliminar la clave "edad"
del informacion_personal["edad"]  # Eliminamos la clave y su valor asociado

# Imprimir el diccionario resultant
print("Diccionario Final:", informacion_personal)