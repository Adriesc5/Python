import json

# Leer el archivo JSON
with open('data.json') as file:
    data = json.load(file)

# Manipulación de datos
nombre = data['nombre']
edad = data['edad']
hobbies = data['hobbies']

# Agregar un nuevo hobby
hobbies.append("programar")

# Crear un nuevo diccionario con los resultados
nuevos_datos = {
    "nombre": nombre,
    "edad": edad,
    "hobbies": hobbies
}

# Escribir los resultados en un nuevo archivo JSON
with open('nuevos_datos.json', 'w') as file:
    json.dump(nuevos_datos, file)

print("Lectura de datos desde Json y creación de nuevo archivo modificado")