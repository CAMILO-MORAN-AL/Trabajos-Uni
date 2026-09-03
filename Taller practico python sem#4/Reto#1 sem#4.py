print("---RESTAURANTE---")
cliente= input("Ingrese su nombre: ")
comida= float(input("Ingrese el valor de la comida: "))
bebida= float(input("Ingrese el valor de la bebida: "))
cantidad_personas= int(input("Ingrese la cantidad de personas: "))

Total_de_la_cuenta= float(comida) + float(bebida)
Valor_por_persona= Total_de_la_cuenta / int(cantidad_personas)

print(f"Cliente: {cliente}")
print(f"Total de la cuenta: {Total_de_la_cuenta}")
print(f"Valor por persona: {Valor_por_persona}")