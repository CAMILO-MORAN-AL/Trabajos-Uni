#Reto6

print("---CREAR PERFIL DEL ESTUDIANTE---")
Nombre= input("Ingrese su nombre: ")
Apellido= input("Ingrese su Apellido: ")
Edad= int(input("Ingrese su Edad: "))
Ciudad= input("Ingrese su Ciudad: ")
Universidad= input("Ingrese su Universidad: ")
Carrera= input("Ingrese su Carrera: ")
Semestre= int(input("Ingrese el Semestre: "))
Promedio= float(input("Ingrese su Promedio: "))

nombre_completo=f"{Nombre} {Apellido}"
es_estudiante_activo=True

print("\n===========================================")
print(f"nombre completo: {nombre_completo}")
print(f"Edad:            {Edad}")
print(f"Ciudad:          {Ciudad}")
print(f"Universidad:     {Universidad}")
print(f"Carrera:         {Carrera}")
print(f"Semestre:        {Semestre}")
print(f"Promedio:        {Promedio:.2f}")
print("\n===========================================")

#str: nombre, Apellido, Ciudad, Universidad, Carrera, nombre_completo
#int: edad, Semestre
#float: Promedio
#bool: es_estudiante_activo(True o False)