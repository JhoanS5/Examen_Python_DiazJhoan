from interfaz import menu_principal, menu_opcion1, menu_opcion2, menu_opcion3


#*CODE MAIN*#

while True:
    try:
        menu_principal()
        opcion = int(input("Por favor, elige una opción (1-3):"))
        if opcion == 1:
            while True:
                try:
                    menu_opcion1()
                    opcion_menu1 = input("¿Deseas calcular nuevamente? (S/N)").strip().upper()
                    if opcion_menu1 == "S":
                        continue
                    elif opcion_menu1 == "N":
                        print("\nSaliendo del MENU 1\n")
                        break
                    else:
                        print("Opcion invalida, vuelve a intentarlo")
                except ValueError:
                    print("Error al ingresar el valor requerido")

        elif opcion == 2:
            while True:
                try:
                    menu_opcion2()
                    opcion_menu2 = input("¿Deseas calcular nuevamente? (S/N)").strip().upper()
                    if opcion_menu2 == "S":
                        continue
                    elif opcion_menu2 == "N":
                        print("\nSaliendo del MENU 2\n")
                        break
                    else:
                        print("Opcion invalida, vuelve a intentarlo")
                except ValueError:
                    print("Error al ingresar el valor requerido")
        
        elif opcion == 3:
            menu_opcion3()
            break

        else:
            print("Opcion invalida, vuelve a intentarlo")
            
    except ValueError:
        print("Error: El valor de la opcion no esta permitido")



    


