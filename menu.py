def menu():

    while True:
        print("\n=== Menú de Lista Enlazada ===")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Mostrar lista")
        print("4. Buscar elemento")
        print("5. Eliminar primer elemento")
        print("6. Eliminar por valor")
        print("7. Tamaño de la lista")
        print("8. Invertir lista")
        print("0. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            dato = int(input("Ingrese dato: "))
            lista.insertar_inicio(dato)

        elif opcion == 2:
            dato = int(input("Ingrese dato: "))
            lista.insertar_final(dato)

        elif opcion == 3:
            lista.mostrar()

        elif opcion == 4:
            dato = int(input("Ingrese dato a buscar: "))
            print("Encontrado" if lista.buscar(dato) else "No encontrado")

        elif opcion == 5:
            lista.eliminar_inicio()

        elif opcion == 6:
            dato = int(input("Ingrese dato a eliminar: "))
            lista.eliminar_por_valor(dato)

        elif opcion == 7:
            print("Tamaño:", lista.tamaño())

        elif opcion == 8:
            lista.invertir()
            print("Lista invertida")

        elif opcion == 0:
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


# Ejecutar el programa
menu()