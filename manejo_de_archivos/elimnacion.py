#Eliminar archivo.txt

import os
if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")
    print("el archivo ha sido eliminado")
else:
    print("el archivo no existe")