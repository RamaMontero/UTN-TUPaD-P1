#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for numero in range(0, 101):
    print(numero)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("El número tiene", cantidad_digitos, "dígito(s).")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))
limite_inferior = min(inicio, fin) + 1
limite_superior = max(inicio, fin)
suma = sum(range(limite_inferior, limite_superior))
print("La suma de los números entre", inicio, "y", fin, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
sumatoria = 0
while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    
    if numero == 0:
        break
    sumatoria += numero
print("La suma total es:", sumatoria)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_secreto = random.randint(0, 9)
intentos = 0
print("Adivina el número (entre 0 y 9):")
while True:
    intento = int(input("Tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for numero in range(100, -1, -2):
    print(numero)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Ingresa un número entero positivo: "))
if numero < 0:
    print("Debes ingresar un número positivo.")
else:
    suma = sum(range(0, numero + 1))
    print("La suma de los números desde 0 hasta", numero, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
# Inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad_numeros = 100
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i+1} de {cantidad_numeros}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\nResultados:")
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
numeros = []
suma_total = 0
cantidad_numeros = 100
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i+1} de {cantidad_numeros}: "))
    numeros.append(numero)
    suma_total += numero
media = suma_total / cantidad_numeros
print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]
print("El número invertido es:", numero_invertido)