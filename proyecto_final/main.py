#Proyecto final Happy Burguer

def MenuPrincipal():
    opcion = ""
    
    while opcion != "s":
        print("Bienvenidos a Happy Burguer!")
        print("a. Pedidos")
        print("b. Clientes")
        print("c. Menu")
        print("s. Salir")
        
        opcion = input("\n Selecciona una opcion: \n")
        
        if opcion == "a":
            #print("Elegiste Pedidos")
            #Se ejecuta productos
            captura_productos()
        elif opcion == "b":
            print("Elegiste Clientes")
        elif opcion == "c":
            print("Elegiste Menu")
        elif opcion == "s":
            print("Elegiste Salir")
        else:
            print("La opcion es Invalida")
            
def captura_productos():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    unidades =int(input("Ingresa el numero de unidades a pedir "))  
    #total_pedido = precio * unidades
    
    print("\nDATOS DEL PEDIDO\n")
    print("Tu producto es: ",nombre)
    print("El precio unitario es: ",precio)
    print("El total de unidades :",unidades)
    print("El total del pedido es: ",calculo_total_pedido(precio,unidades))


def calculo_total_pedido(x,y):
    return x * y
    
            
#Inicia la ejecucion del menu
MenuPrincipal()