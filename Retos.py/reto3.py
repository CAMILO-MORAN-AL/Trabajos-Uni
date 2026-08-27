#Reto3
print("---Calcular Indice de Masa Corporal")
Nombre= input("Ingrese su nombre: ")
Kg= float(input("Ingrese su Peso en Kilogramos: "))
Estatura= float(input("Ingrese su Altura en Metros: "))

IMC= Kg/(Estatura**2)

print("---Indice de Masa Corporal---")
print("Nombre: ", Nombre)
print("Peso: ", Kg)
print("Estatura: ", Estatura)
print("IMC: ", IMC)