# 1. Crear menú para acceder a diferentes funciones
# 2. Opcion 1 para añadir a la lista
# 3. Ver lista
# 4. salir del programa
# 5. eliminar obejetos de la lista


lista = []

while True:
    
    print("Menu"
    "\n 1. Añadir a la lista"
    "\n 2. Ver lista"
    "\n 3. Salir"
    "\n 4. Eliminar objetos" \
    "\n")

    opcion = input("ingrese una opcion: ")
    
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion!= "4":
        print("Opción no válida. Por favor, selecciona una opción válida.\n")

    elif opcion == "1":
        while True:
            user_input = input("Ingresa algo a la lista: ").lower()
    
            if user_input == "salir":
                break
    
            lista.append(user_input)
                

    elif opcion == "2":
        while True:
            if lista == []:
                print("La lista esta vacia")
                user_input = input("Escribe '9' para volver al menu: ").lower()
                if user_input == "9":
                    break

            else:
                print("La lista es: ", lista)
                break
                

    elif opcion == "3":
        print("Adios!!")
        break

    elif opcion == "4":

        print("Indique que valor quiere eliminar de la lista: ")
        user_input = input()
        lista.remove(user_input)
    
    else:
        print("Opcion invalida")