import csv

# Abrir el archivo CSV en modo de lectura
with open('peliculas.csv', 'r') as file:
    # Leer el archivo CSV
    reader = csv.reader(file)

    # Iterar sobre las filas del archivo
    for row in reader:
        # Procesar cada fila
        # row es una lista que contiene los valores de cada columna en la fila actual
        print(row)  # Ejemplo: Imprimir cada fila

# Abrir un archivo CSV en modo de escritura
with open('peliculas.csv', 'a', newline='') as file:
    # Crear el escritor CSV
    writer = csv.writer(file)

    # Escribir filas en el archivo CSV
    # writer.writerow(['Título', 'Género', 'Director', 'Año', 'Duración'])  # Escribir encabezados, solo si está vacío el archivo
    writer.writerow(['El Rey León', 'Animación', 'Roger Allers, Rob Minkoff', '1994', '88 min']) # Agregando películas
    writer.writerow(['El Mago de Oz', 'Fantasía', 'Victor Fleming', '1939', '102 min'])

print("¡Listas tus nuevas películas!")