# 1. Crear menú para acceder a diferentes funciones
# 2. Opcion 1 para añadir a la lista
# 3. Opcion 2 Ver lista
# 4. opcion 3 Eliminar objetos de la lista
# 5. opcion 4 Ordenar la lista

def add_to_list(lista):
    print("Para salir en cualquier momento favor de presionar el #9")
    while True:

        user_input = input("\nIngresa algo a la lista: ").lower()

        if user_input == "9":
            break

        lista.append(user_input)

def view_list(lista):
        
    if lista == []:
        print("La lista esta vacia")
                    

    else:
        print("La lista es: ", lista)
        

def remove_from_list(lista):

    if lista == []:
        print("La lista esta vacia")
    else:
        print("La lista es: ", lista)
        user_input = input("Indique que valor quiere eliminar de la lista: ").lower()
        if user_input in lista:
            lista.remove(user_input)
        else:
            print("El valor no esta en la lista")

def sorted_list(lista):

    if lista == []:
        print("No hay contenido en la lista \n")

    else:
        
        lista.sort()
        print("la lista ordenada es: ", lista)

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
            add_to_list(lista)
                

        elif opcion == "2":
            view_list(lista)
                

        elif opcion == "3":
            remove_from_list(lista)

        elif opcion == "4":
            sorted_list(lista)

        elif opcion == "5":
            print("Adios!!")
            break

        else:
            print("Opcion invalida")

if __name__ == "__main__":

    main()