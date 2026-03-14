import lista_ops

def main():

    lista = []

#Menu principal para el usuario
    while True:
    
        print("Menu"
        "\n 1. Añadir a la lista"
        "\n 2. Ver lista"
        "\n 3. Eliminar objetos"
        "\n 4. Ordenar lista"
        "\n 5. Salir"
        "\n")

        opcion = input("ingrese una opcion: ")
    
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion!= "4" and opcion!= "5":
            print("Opción no válida. Por favor, selecciona una opción válida.\n")

        elif opcion == "1":
            lista_ops.add_to_list(lista)
                

        elif opcion == "2":
            lista_ops.view_list(lista)
                

        elif opcion == "3":
            lista_ops.remove_from_list(lista)

        elif opcion == "4":
            lista_ops.sorted_list(lista)

        elif opcion == "5":
            print("Adios!!")
            break

        else:
            print("Opcion invalida")

if __name__ == "__main__":

    main()