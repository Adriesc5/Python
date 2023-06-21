import csv

# Datos de ejemplo
datos = [
    ['Título', 'Género', 'Director', 'Año', 'Duración'],
    ['Titanic', 'Romance', 'James Cameron', '1997', '195 min'],
    ['El Padrino', 'Drama', 'Francis Ford Coppola', '1972', '175 min'],
    ['Jurassic Park', 'Ciencia ficción', 'Steven Spielberg', '1993', '127 min'],
    ['Pulp Fiction', 'Crimen', 'Quentin Tarantino', '1994', '154 min'],
    ['El Señor de los Anillos: La Comunidad del Anillo', 'Fantasía', 'Peter Jackson', '2001', '178 min'],
    ['La La Land', 'Musical', 'Damien Chazelle', '2016', '128 min'],
    ['Matrix', 'Ciencia ficción', 'Lana Wachowski, Lilly Wachowski', '1999', '136 min'],
    ['Ciudadano Kane', 'Drama', 'Orson Welles', '1941', '119 min'],
]

# Nombre del archivo CSV
nombre_archivo = 'peliculas.csv'

# Abrir el archivo CSV en modo de escritura
with open(nombre_archivo, 'w', newline='') as file:
    # Crear el escritor CSV
    writer = csv.writer(file)

    # Escribir los datos en el archivo CSV
    for registro in datos:
        writer.writerow(registro)

print(f"Se ha generado el archivo CSV '{nombre_archivo}' con datos de ejemplo.")