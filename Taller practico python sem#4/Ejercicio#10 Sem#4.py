print("---SALARIO DE UN TRABAJADOR---")
empleado= input("Ingrese el nombre del trabajador: ")
horas_trabajadas= int(input("Ingrese las horas trabajadas: "))
pago_por_hora= float(input("Ingrese el pago por hora: "))

salario= horas_trabajadas * pago_por_hora

print(f"Empleado: {empleado}")
print(f"Salario: {salario}")