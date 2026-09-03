print("---Factura Sencilla---")
nombre_cliente = input("Ingrese su nombre: ")
producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = precio_producto * cantidad
IVA = subtotal * 0.19  
total = subtotal + IVA

print("-----Factura-----")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: {precio_producto}")
print(f"Cantidad: {cantidad}")
print(f"\nSubtotal: {subtotal}")
print(f"IVA: {IVA}")
print(f"Total: {total}")