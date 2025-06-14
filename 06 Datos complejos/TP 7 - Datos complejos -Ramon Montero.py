#Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

nombres_frutas = list(precios_frutas.keys())

print(nombres_frutas)

#Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}

print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

print("\nContactos cargados correctamente.")

busqueda = input("\nIngresá el nombre del contacto que querés buscar: ")

if busqueda in agenda:
    print(f"El número de {busqueda} es: {agenda[busqueda]}")
else:
    print("Contacto no encontrado.")

# Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("\nPalabras únicas:")
print(palabras_unicas)

print("\nFrecuencia de palabras:")
print(frecuencia_palabras)

# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}


for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumnos[nombre] = tuple(notas)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {"Ana", "Luis", "Pedro", "María", "Sofía"}
parcial_2 = {"Pedro", "María", "Julián", "Camila", "Sofía"}

ambos = parcial_1 & parcial_2
print("Aprobaron ambos parciales:")
print(ambos)

solo_uno = parcial_1 ^ parcial_2
print("\nAprobaron solo uno de los dos:")
print(solo_uno)

al_menos_uno = parcial_1 | parcial_2
print("\nAprobaron al menos un parcial:")
print(al_menos_uno)

#Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

stock_productos = {
    "manzanas": 10,
    "peras": 5,
    "bananas": 12
}

producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")
    agregar = int(input("¿Cuántas unidades querés agregar al stock?: "))
    stock_productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
else:
    nuevo_stock = int(input(f"{producto} no está en el inventario. Ingresá el stock inicial: "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} fue agregado con {nuevo_stock} unidades")

print("\nStock actualizado:")
for prod, cantidad in stock_productos.items():
    print(f"{prod}: {cantidad}")

#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {}

for i in range(3):
    dia = input("Ingresá el día (ej: lunes): ").lower()
    hora = input("Ingresá la hora (ej: 14:00): ")
    evento = input("Ingresá el evento: ")
    
    clave = (dia, hora)
    agenda[clave] = evento
    print(f"Evento agregado para {dia} a las {hora}.\n")

print("Agenda completa:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia.title()} a las {hora}: {evento}")

#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario invertido (capital -> país):")
print(capitales_paises)