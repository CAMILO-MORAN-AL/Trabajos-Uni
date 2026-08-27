#Reto5
#nombre = input("Ingrese su nombre: ")
#edad = input("Ingrese su edad: ")
#nueva_edad = edad + 5
#print(nombre)
#print(nueva_edad)


#1. ¿Qué problema presenta el código?
#El codigo presenta Problema a la hora de solicitar la edad al usuario, ya que si se guarda pero,
#a la hora de Usarlo para calcular la nueva edad va presentar un error porque al ser guardado con (input) sin nada mas previamente, se guarda como un dato de tipo (str)
#Causando que al hacer el calculo no se haga efectivo porque no hay ningun dato numerico guardado para ser usado de forma matematica, sino de forma textual.

#2. ¿Qué tipo de dato devuelve input()?
#Siempre va a devolver un dato de tipo (str) independientemente de si se guarda numero o letras.

#3. ¿Cómo se puede corregir?
#Agregandole a la variable edad despues del (=) la funcion int() permitiendo que este si guarde el numero para ser usado para operaciones matematicas.

#4. Escriba el código corregido.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nueva_edad = edad + 5
print(nombre)
print(nueva_edad)
