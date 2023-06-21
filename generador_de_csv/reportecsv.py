import json
import csv

class lectorJSON:
    def obtenerJSON(self, nombre_archivo):
        datos ={}
        try:
            with open(nombre_archivo) as archivo:
                datos = json.load(archivo)
        except: Exception as e:
            print('Error al leer al archivo: {}'.format(e))
        return datos
    