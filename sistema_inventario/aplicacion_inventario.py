from sistema_inventario.administracion_inventario import AdministracionInventario

class Aplicacion:
    
    def __init__(self):
        self.iniciarAplicacion()
    
    def iniciarAplicacion(self):
        inventario = AdministracionInventario()
        print("------------------------------------")
        print("Bienvenido al sistema de Inventarios")
        salir_programa = False
        while not salir_programa:
            print("Menú del inventario")
            print(""" 
                1.- Mostrar lista de productos
                2.- Agregar producto
                3.- Modificar producto
                4.- Eliminar producto
                5.- Salir del programa
                """)
            opcion = int(input("Indica una opción del menú "))
            if opcion == 1:
                inventario.mostrarListaProductos()
            elif opcion == 2:
                inventario.agregarProducto()
            elif opcion == 3:
                inventario.modificarProducto()
            elif opcion == 4:
                inventario.eliminarProducto()
            if opcion == 5:
                print("Salida del programa, hasta luego ")
                salir_programa = True
                
sistema_inventario = Aplicacion()