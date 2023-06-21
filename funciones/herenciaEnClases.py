# Definir la clase "base" Publicación

class Publicacion:
    def __init__(self, titulo, autor, fecha):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
    
    def imprimir_info(self):
        
        print("Título: ",self.titulo)
        print("Autor: ", self.autor)
        print("Fecha: ", self.fecha)
        
# Definimos una clase llamada Libro que contiene los atributos de Publicación

class Libro(Publicacion):
    def _init_ (self, titulo, autor, fecha, editorial):
        super()._init_(titulo, autor, fecha)
        self.editorial = editorial
        
    def imprimir_info(self):
        super().imprimir_info()
        print("Editorial: ", self.editorial)
        
# Definimos una clase llamada Revista que contiene los atributos de Publicación

class Revista(Publicacion):
    def _init_ (self, titulo, autor, fecha, numero):
        super()._init_ (titulo, autor, fecha)
        self.numero = numero
    
    def imprimir_info(self):
        super().imprimir_info()
        print("Número: ",self.numero)
        
# Creamos una nueva instancia u objeto utilizando la clase Libro

Quijote = Libro("El Quijote de La Mancha","Miguel de Cervantes",1605,"Planeta")
Quijote.imprimir_info()