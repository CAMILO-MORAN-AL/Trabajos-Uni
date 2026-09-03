#1 ¿Qué función se utiliza en Python para pedir datos al usuario? 
# la funcion input() es la utilizada para pedir datos al usuario en Python.
#2 ¿Qué tipo de dato devuelve input() por defecto?
# Siempre va a devolver un tipo de dato string.
#3 ¿Qué diferencia existe entre int() y float()? 
# int() convierte un valor a un número entero, mientras que float() convierte un valor a un número decimal.
#4 ¿Para qué sirve el operador + cuando se trabaja con cadenas? 
# sirve para unir dos o más cadenas de texto en una sola.
#5 ¿Cuál es la diferencia entre / y // en Python? 
#(/) realiza división normal y devuelve un número decimal.
#(//) realiza una división entera y devuelve solo la parte entera del resultado.




nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
Ciudad= input("Ingrese su Ciudad: ")

print(f"Hola, {nombre} tienes {edad} años y vives en {Ciudad}.")