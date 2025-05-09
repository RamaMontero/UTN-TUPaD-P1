#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int (input ("Ingrese su edad: ")) 
if edad > 18:
    print ("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 
nota = float (input ("Ingrese su nota: ")) 
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Por favor, ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 
edad = int (input ("Ingrese su edad: ")) 
if edad < 12:
    print ("Pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print ("Pertenece a la categoria Adolecente")
elif edad >= 18 and edad < 30:
    print ("Pertenece a la categoria Adulto/a joven")
else:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.  

#La función len() devuelve la cantidad de caracteres (o elementos) de un string, lista, o cualquier estructura iterable.
contraseña = input("Por favor, ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random 
from statistics import mean, median, mode, StatisticsError
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista de números aleatorios:")
print(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = "indefinida (hay más de una moda)"
print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if isinstance(moda, (int, float)):
    if media > mediana > moda:
        print("Sesgo positivo (a la derecha)")
    elif media < mediana < moda:
        print("Sesgo negativo (a la izquierda)")
    elif media == mediana == moda:
        print("Sin sesgo")
    else:
        print("No se puede determinar un sesgo claro")
else:
    print("No se puede determinar el sesgo porque la moda es indefinida")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 
frase = input ("Ingrese una frase: ")
if frase[-1].lower() in 'aeiou':
    frase += '!'
print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
print("Elija una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la Primera Letra en Mayúscula")
opcion = input("Ingrese el número de la opción (1, 2 o 3): ")
if opcion == "1":
    print(nombre.upper()) #upper(): Convierte todo el texto a mayúsculas.
elif opcion == "2":
    print(nombre.lower()) #lower(): Convierte todo el texto a minúsculas.
elif opcion == "3":
    print(nombre.title()) #title(): Convierte la primera letra de cada palabra a mayúscula.
else:
    print("Opción no válida. Debe ingresar 1, 2 o 3.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Periodo del año Desde el 21 de diciembre hasta el 20 de marzo (incluidos)= Estación en el hemisferio norte es invierno y Estación en el hemisferio sur es Verano
# Periodo del año Desde el 21 de marzo hasta el 20 de junio (incluidos) = Estación en el hemisferio norte es Primavera y Estación en el hemisferio sur es Otoño
# Periodo del año Desde el 21 de junio hasta el 20 de septiembre (incluidos) = Estación en el hemisferio norte es Verano y Estación en el hemisferio sur es Invierno
# Periodo del año Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) = Estación en el hemisferio norte es Otoño y Estación en el hemisferio sur es Primavera
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1 a 12): "))
dia = int(input("Ingresa el día del mes: "))
def obtener_estacion(mes, dia, hemisferio):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano" if hemisferio == "N" else "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        return "Otoño" if hemisferio == "N" else "Primavera"
    else:
        return "Fecha no válida"
if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido. Debe ser 'N' o 'S'.")
else:
    estacion = obtener_estacion(mes, dia, hemisferio)
    print(f"La estación es: {estacion}")
