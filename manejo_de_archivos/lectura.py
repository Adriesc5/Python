#LECTURA DE ARCHVOS
archivo = open("archivo.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()