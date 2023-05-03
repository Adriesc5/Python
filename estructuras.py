#Adrian Escobedo el mas perro
#05/01/2023

#crear una lista
lista =["Lunes","Martes","Miercoles"]
print(lista)
lista.append("Jueves")#agrega
lista.extend(["Viernes","Sabado"])
print(lista)
lista.remove("Martes")#busca el valor y lo elimina 
lista.pop(3)#elimina el 4 valor por que 0,1,2,3

#crear una tupla, son estructuras fijas, no se pueden modificar, no se pueden borrar o agregar elementos
deportes =("futbol","ping-pong","Basquetbol")
type(deportes)
#crar un diccionario
#tienen dos elementos, llave y valor
dicNumeros ={1:"Texto",2:25.36,3:True,4:12}
type(dicNumeros)

#crear un conjunto(sets)
conjunto = {2,4,8,3}
type(conjunto)
conjunto.add(7)
conjunto
