#ejercicio6
print("--Calculadora de Edad--")
print("Se calculara de forma aproximada la edad que tienes.")

nombre= input("Ingrese su nombre: ")
AñoDeNacimiento= float(input("Ingrese su año de Nacimiento: "))
AñoActual= float(input("Ingrese el año Actual: "))

Edad = AñoActual - AñoDeNacimiento

print(f"{nombre}, Tiene aproximadamente {Edad}, años")