# 1 Crear una variable de tipo lista de cadenas
panaderia = ["pan", "galletas", "pasteles", "tortas", "donuts"]

# 2 Ejemplo de lista de números
ventas_hora = [10, 20, 30, 15]

# 3 Ejemplo de lista con valores mixtos
valores_mixtos = ["10", 20, 30.5, True]

# 4. Acceder a un elemento de la lista por índice
producto_escogido = panaderia[3]

# 5. Acceder a un último elemento de la lista
ultimo_producto = panaderia[-1]

# 6. Agregar un elemento al final de la lista
panaderia.append("croissant")
print(f"ultimo producto agregado: {panaderia}")

# 7. Actualizar o modificar un elemento de la lista
panaderia[0] = "pan integral"
print(f"producto actualizado: {panaderia}")

# 8. Eliminar un elemento de la lista por valor
panaderia.remove("donuts")
print(f"producto eliminado: {panaderia}")

# 9. Eliminar un elemento de la lista por índice
del panaderia[2]
print(f"producto eliminado por índice: {panaderia}")

# 10. Obtener la longitud de la lista
longitud_lista = len(panaderia)
print(f"longitud de la lista: {longitud_lista}")