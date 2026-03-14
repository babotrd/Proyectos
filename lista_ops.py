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
