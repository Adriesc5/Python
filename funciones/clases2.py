"""#Crear clases de perros

class perro:
    #Metodo init (para inicializar valores) contructores
    def __init__(self,nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        pass
    
    def ladrar(self):
        print(f"{self.nombre}: Wof")
        pass
        
#metodo datos
    def datos(self):
        print(f"nombre: {self.nombre}, edad: {self.edad}")
        pass
nuevo_perro = perro("Firulais",3)

nuevo_perro.ladrar()

nuevo_perro.datos()

perro_perron = perro("LMV",3)
perro_perron.datos()"""

class clase_cubo:
  def __init__(self, color, textura):
    self.color = color
    self.textura = textura
  
  # Funcion para mostrar las caracteristicas del cubo
  def mostrar_cubo(self):
    print("El cubo es de color " + self.color)
    print("La textura que tiene es de " + self.textura)
  
  # definir color
  def setColor(self, color_nuevo):
    self.color = color_nuevo
  
  # Esta funcion sirve para cambiar la variable "textura" del cubo
  def setTextura(self, textura_nueva):
    self.textura = textura_nueva
  
  # Obtener color
  def getColor(self):
    return self.color
  
  # Obtener textura
  def getTextura(self):
    return self.textura

print("Vamos a definir un cubo")
color = input("\n Que color quieres que tenga el cubo? \n")
textura = str(input("\n Que textura quieres que tenga el cubo? \n"))
cubo = clase_cubo(color, textura)

cubo.mostrar_cubo()

opcion = ""
print("Opciones para trabajar con el cubo")
print("a. Cambiar color")
print("b. Cambiar textura")
print("s. Salir")
opcion = input("\nSelecciona una opcion:\n")


opcion = ""
print("Opciones para trabajar con el cubo")
print("a. Cambiar color")
print("b. Cambiar textura")
print("c. Mostrar cubo")
print("s. Salir")

while opcion != "s":
  opcion = input("\n Selecciona una opcion, para ver el menu escribe la letra 'm': \n")

  if opcion == "a":
    color_nuevo = input("\nInserta el color nuevo\n")
    cubo.setColor(color_nuevo)
  elif opcion == "b":
    textura_nueva = input("\nInserta la textura nueva\n")
    cubo.setTextura(textura_nueva)
  elif opcion == "c":
    cubo.mostrar_cubo()
  elif opcion == "s":
    print("\nGracias por correr este programa")
  elif opcion =="m":
    print("Opciones para trabajar con el cubo")
    print("a. Cambiar color")
    print("b. Cambiar textura")
    print("c. Mostrar cubo")
    print("s. Salir")
  else:
    print("\nOpcion no encontrada\n")