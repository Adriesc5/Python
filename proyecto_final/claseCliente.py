#Definición de clase Cliente, para uso en programa Happy Burger

class Cliente:
    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        self.clave = clave
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono

def agregar_cliente(self, clave):
    pass

def eliminar_cliente(self, clave):
    pass

def actualizar_cliente(self, clave):
    pass

''' Llamado a las funciones que operan con las clases y sus datos '''

#Programa principal

manejo_clientes = ManejoClientes()

# Agregar un cliente
manejo_clientes.agregar_cliente("123", "Juan Perez", "Calle 123", "juan@example.com", "555-1234")

# Eliminar un cliente
manejo_clientes.eliminar_cliente("123")

# Actualizar un cliente
manejo_clientes.actualizar_cliente("456")