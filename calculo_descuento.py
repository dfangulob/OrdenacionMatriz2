## definir la funcion

def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

## llamar el valor predeterminado del 10%
monto_total = 1000  # Ejemplo de monto
descuento1 = calcular_descuento(monto_total)
monto_final1 = monto_total - descuento1
print(f"Descuento: {descuento1}, Monto final a pagar: {monto_final1}")

# Llamada 2: especificando un porcentaje de descuento diferente
porcentaje_descuento = 20  # Ejemplo con 20% de descuento
descuento2 = calcular_descuento(monto_total, porcentaje_descuento)
monto_final2 = monto_total - descuento2
print(f"Descuento: {descuento2}, Monto final a pagar: {monto_final2}")