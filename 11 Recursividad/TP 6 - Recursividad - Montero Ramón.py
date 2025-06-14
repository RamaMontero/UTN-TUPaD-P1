#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

n = int(input("Ingrese un número: "))
mostrar_factoriales(n)

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. 

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_serie_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")

n = int(input("Ingrese hasta qué posición desea la serie de Fibonacci: "))
mostrar_serie_fibonacci(n)

#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

#Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")

#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print(f"Suma de dígitos: {suma_digitos(numero)}")

#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques del nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(nivel)}")

#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")