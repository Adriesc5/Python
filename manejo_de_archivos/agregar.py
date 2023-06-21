archivo = open("nuevo_archivo.txt", "a")
contenido_nuevo = "\n Nueva linea agregada"
archivo.write(contenido_nuevo)
print(contenido_nuevo)
archivo.close()