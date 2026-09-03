print("---VENTA---")
nombre_vendedor = input("Ingrese el nombre del vendedor: ")
nombre_cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad vendida: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

subtotal = cantidad * precio_unitario
descuento = subtotal * 0.10
subtotal_con_descuento = subtotal - descuento
IVA = subtotal_con_descuento * 0.19
total_final = subtotal_con_descuento + IVA

print("\n---DETALLE DE LA VENTA---")
print(f"Vendedor: {nombre_vendedor}")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"\nSubtotal: {subtotal}")
print(f"Descuento: {descuento}")
print(f"IVA: {IVA}")
print(f"\nTotal a pagar: {total_final}")