from arbol import ArbolBinario

# Crear un árbol binario
arbol = ArbolBinario()
option = 0

while option != 10:
    option = int(input("Select an option: \n"
                       "1. Add node\n"
                       "2. Search node\n"
                       "3. Update node\n"
                       "4. Delete node\n"
                       "5. Show in order\n"
                       "6. Show pre order\n"
                       "7. Show post order\n"
                       "8. Show min\n"
                       "9. Show max\n"
                       "10. Exit"))
    match option:
        case 1:
            node = int(input("Enter the new node: "))
            arbol.agregar(node)
        case 2:
            node = int(input("Enter the node to search: "))
            arbol.search(node)
              
        case 3:
            node = int(input("Enter the node to update: "))
            new = int(input("Enter the new node: "))
            arbol.update(node, new)
        case 4:
            node = int(input("Enter the node to delete: "))
            arbol.delete(node)
        case 5:
            arbol.in_order_traversal()
        case 6:
            arbol.pre_order()
        case 7:
            arbol.post_order()
        case 8:
            arbol.search_min()
        case 9:
            arbol.search_max()
        case 10:
            print("Good bye...")
        case _:
            print("Invalid option")



