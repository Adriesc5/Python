# Programa para cafetera automática

class Menu: # Clase que contiene las bebidas y sus atributos

    #Aquí van los atributos
    
    bebidas = {
        "expreso": {
            "nombre": "Expreso",
            "costo": 10.50,
            "ingredientes": {
                "agua": 50,
                "café": 20
            }
        },
        "latte": {
            "nombre": "Latte",
            "costo": 12.80,
            "ingredientes": {
                "agua": 100,
                "leche": 50,
                "café": 16
            }
        },
        "capuchino": {
            "nombre": "Capuchino",
            "costo": 15.00,
            "ingredientes": {
                "agua": 100,
                "leche": 100,
                "café": 18
            }
        },
        "americano": {
            "nombre": "Americano",
            "costo": 8.75,
            "ingredientes": {
                "agua": 120,
                "café": 24
            }
        }
    }  
     
    @staticmethod 
    
    # Es un método que pertenece a esta clase, no requiere instancias para su uso, tampoco 
    # requiere self, sirve para clarificar el uso de las clases para los usuarios

    def obtener_menu(): # Muestra el menú en la pantalla al inicio
        print(" MENÚ DE BEBIDAS ")
        for bebida, detalles in Menu.bebidas.items():
            print(f"{bebida.capitalize()}: {detalles['nombre']} - Costo: ${detalles['costo']:.2f}")
      
        
    @staticmethod
    def buscar_bebida(tipo_bebida): # Muestra los detalles de la bebida seleccionada
        bebida = Menu.bebidas.get(tipo_bebida)
        if bebida:
            print(f"\nBebida: {bebida['nombre']}")
            print("Ingredientes:")
            for ingrediente, cantidad in bebida["ingredientes"].items():
                print(f"{ingrediente.capitalize()}: {cantidad}")
            print(f"Costo: ${bebida['costo']:.2f}")
        else:
            print("Bebida no encontrada en el menú.")
        
        
class MaquinaCafetera: # Ejecuta el cobro y regresa el cambio
    def __init__(self):
        self.menu = Menu()
        self.total_insertado = 0.0

    def pago(self,costo):
        self.total_insertado = 0.0
        while self.total_insertado < costo:
            moneda = float(input("Inserte moneda (10, 5, o 1): "))
            if moneda not in [10, 5, 1]:
                print("Moneda no válida. Intente de nuevo.")
            else:
                self.total_insertado += moneda

        if self.total_insertado >= costo:
            print("Pago aceptado.")
            return True
        else:
            print("Pago insuficiente.")
            return False
              
    def devuelvecambio(self,costo):
        cambio = self.total_insertado - costo
        if cambio > 0:
            print(f"Devolviendo cambio: ${cambio:.2f}")
            return cambio
        else:
            print("No requiere cambio")
            return 0.0
    
# Menú Principal
sigue = True
while sigue:
    
    maquina = MaquinaCafetera()
    maquina.menu.obtener_menu()
    tipo_bebida = input("Seleccione el tipo de café que desea:")
    maquina.menu.buscar_bebida(tipo_bebida.lower())
    costo = maquina.menu.bebidas.get(tipo_bebida.lower(), {}).get("costo", 0)
    if costo > 0:
        if maquina.pago(costo):
            print("Sirviendo café.")
            maquina.devuelvecambio(costo)
        else:
            print("Transacción cancelada.")    
    respuesta = input("\n¿Deseas pedir algo más? (s/n)\n")
    if respuesta.lower() != 's':
        sigue = False
        print("Gracias por tu compra")
        #break