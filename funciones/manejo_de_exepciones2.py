try:
    archivo =open("archivo.txt","r")
    
#lectura para un archivo externo
except FileNotFoundError:
    print("Archivo no se encuentra")