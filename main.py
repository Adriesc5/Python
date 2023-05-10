print("Bienvenido a Happy burger,\n Seleccione la opcion deseada:\n a. Pedidos\n b. Clientes\n c. Menú\n d. Salir")
opcion_menu = str(input("Que opcion eliges?\n"))

if opcion_menu == "a":
    print("pedidos")
elif opcion_menu =="b":
    print("Clientes")
elif opcion_menu =="c":
    print("Menu")
elif opcion_menu =="d":
    print("Salir")
else:
    print("Seleccione una opcion correcta")
    opcion_menu = str(input("Que opcion eliges?\n"))