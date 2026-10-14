def sistema_taller():
    matriz = [["" for _ in range(6)] for _ in range(30)]
    total_vehiculos = 0

    while True:
        print("\n--------------------------")
        print("Sistema de Taller de Reparación de Vehículos")
        print("----------------------------")
        print("1. Registrar vehículo")
        print("2. Mostrar todos los vehículos registrados")
        print("3. Salida y días de reparación")
        print("4. Vehículos terminados")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if total_vehiculos < 30:
                print(f"\nRegistro del vehículo {total_vehiculos + 1}:")
                placa = input("Ingrese la placa del vehículo: ")
                nombre = input("Ingrese el nombre del propietario: ")
                celular = input("Ingrese el número de celular del propietario: ")
                fecha_ingreso = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")

                matriz[total_vehiculos][0] = placa
                matriz[total_vehiculos][1] = nombre
                matriz[total_vehiculos][2] = celular
                matriz[total_vehiculos][3] = fecha_ingreso
                matriz[total_vehiculos][4] = "En reparación"
                matriz[total_vehiculos][5] = ""

                total_vehiculos += 1
                print("Vehículo registrado exitosamente.")
            else:
                print("No se pueden registrar más vehículos. Capacidad máxima alcanzada.")

        elif opcion == "2":
            if total_vehiculos == 0:
                print("No hay vehículos registrados.")
            else:
                print("\nVehículos registrados:")
                for i in range(total_vehiculos):
                    print(f"Vehículo {i + 1}:")
                    print(f"Placa: {matriz[i][0]}")
                    print(f"Nombre del propietario: {matriz[i][1]}")
                    print(f"Celular del propietario: {matriz[i][2]}")
                    print(f"Fecha de ingreso: {matriz[i][3]}")
                    print(f"Estado: {matriz[i][4]}")
                    print(f"Días de reparación: {matriz[i][5]}")
                    print("----------------------------")

        elif opcion == "3":
            if total_vehiculos == 0:
                print("No hay vehículos registrados.")
            else:
                print("\nSalida y días de reparación:")
                for i in range(total_vehiculos):
                    if matriz[i][4] == "En reparación":
                        fecha_salida = input(f"Ingrese la fecha de salida del vehículo {matriz[i][0]} (dd/mm/aaaa): ")
                        matriz[i][5] = fecha_salida
                        matriz[i][4] = "Reparación terminada"
                        print(f"Vehículo {matriz[i][0]} ha salido del taller.")

        elif opcion == "4":
            if total_vehiculos == 0:
                print("No hay vehículos registrados.")
            else:
                print("\nVehículos terminados:")
                for i in range(total_vehiculos):
                    if matriz[i][4] == "Reparación terminada":
                        print(f"Vehículo {i + 1}:")
                        print(f"Placa: {matriz[i][0]}")
                        print(f"Nombre del propietario: {matriz[i][1]}")
                        print(f"Celular del propietario: {matriz[i][2]}")
                        print(f"Fecha de ingreso: {matriz[i][3]}")
                        print(f"Fecha de salida: {matriz[i][5]}")
                        print("----------------------------")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
    