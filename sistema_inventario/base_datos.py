import sqlite3 
import os

class BaseDatos:
    
    def __init__(self, nombreBaseDatos):
        self.nombreBaseDatos = nombreBaseDatos
        
    def crearBaseDatos(self):
        try:
            conn = sqlite3.connect(self.nombreBaseDatos) 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))
        #cerificar que existe
    def verificarBaseDatosExiste(self):
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False
    #crear la tabla de productos
    def crearTablaProductos(self):
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE productos
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_producto TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio FLOAT NOT NULL,
            stock INTEGER NOT NULL
            );''')
        
        conexion.close()
    #Abre la conexion con la base de datos y marca error si no existe
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos) 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))
            
            