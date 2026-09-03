print("---COMPRA EN TIENDA---")
producto= input("Ingrese el nombre del producto: ")
precio= float(input("Ingrese el precio del producto: "))
cantidad= int(input("Ingrese la cantidad del producto: "))

total= precio * cantidad

print(f"Producto: {producto}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Total a pagar: {total}")