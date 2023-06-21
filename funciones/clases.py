#Definicion de clase
class Auto:
    def __init__(self):
        self.color ="Rojo" #Queda dentro de la clase
        self.marca ="vm" # Es una variable local
        
        pass
#Crear un objeto a partir de clase Auto

auto_adrian = Auto()
print(auto_adrian.color) # Rojo
print(auto_adrian.marca) #?