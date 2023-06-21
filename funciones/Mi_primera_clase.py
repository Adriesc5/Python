# Crear clase general de Vehículos

class Vehiculo:
    def _init_(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def obtener_caracteristicas(self):
        return self.color, self.ruedas
    
class Carro(Vehiculo):
    def _init_ (self, color, ruedas, velocidad, cilindrada):
        super()._init_(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def obtener_caracteristicas(self):
        color_y_ruedas = super().obtener_caracteristicas()
        return color_y_ruedas + (self.velocidad, self.cilindrada)
    
# Creación de un carro

Micarro = Carro("Blanco",4,200,4)

# Arreglo que recibe los atributos de Micarro

Caracteristicas = Micarro.obtener_caracteristicas()

print("Color: ", Caracteristicas[0])
print("Ruedas: ", Caracteristicas[1])
print("Velocidad: ", Caracteristicas[2])
print("Cilindrada: ", Caracteristicas[3])

print(Caracteristicas)