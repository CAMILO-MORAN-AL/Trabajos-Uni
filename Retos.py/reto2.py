#reto2
print("---Generar Factura---")
Nombre= input("Nombre: ")
ValorComida= float(input("Valor de la Comida: "))
ValorBebida= float(input("Valor de la Bebida: "))

Subtotal= ValorComida+ValorBebida
Propina= Subtotal*0.10
Total= Propina+Subtotal

print("---Factura---")
print("-------------")
print("Cliente: ", Nombre)
print("-------------")
print("Valor de la Comida: ", ValorComida)
print("Valor de la Bebida: ", ValorBebida)
print("-------------")
print("Detalles a pagar.")
print("Subtotal: ", Subtotal)
print("Propina: ", Propina)
print("Total a Pagar: ", Total)
