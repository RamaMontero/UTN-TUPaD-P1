# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print ("Hola Mundo!")
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.
nombre = input ("Ingrese su nombre: ")
print (f"Hola {nombre}")
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla.
nombre = input ("Ingrese su nombre nuevamente: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 
radio = float(input ("Ingrese el radio de un circulo para calcular su area y su perímetro: "))
pi = float(3.1416)
area = round(pi * radio ** 2, 2)
perimetro = round(2 * pi * radio, 2)
print (f"El area del circulo es {area}")
print (f"El perimetro del circulo es {perimetro}")
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.
segundos = int(input("Por favor, ingresa una cantidad de segundos y veremos a cuantas horas equivalen: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print (f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos. ")
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número. 
numero = int(input("Ingresa un número entero y veremos su tabla de multiplicar: "))
print (numero * 1)
print (numero * 2)
print (numero * 3)
print (numero * 4)
print (numero * 5)
print (numero * 6)
print (numero * 7)
print (numero * 8)
print (numero * 9)
print (numero * 10)
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
num1 = int(input("Ingrese un número entero distinto a 0: "))
num2 = int(input("Por favor ingrese otro número entero distinto a 0: "))
suma = (num1 + num2)
division = round(num1 / num2, 2)
multiplicacion = (num1 * num2)
resta = (num1 - num2)
print(f"La suma de {num1} y {num2} da como resultado {suma}, al dividirlos el resultado es {division}, la multiplicación da {multiplicacion} y la resta {resta}. ")
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. 
print("Calculemos tu masa corporal")
altura = float(input("Ingresa tu altura (en metros): "))
peso = float(input("Ingresa tu peso (en kilogramos): "))
IMC = round(peso / (altura) ** 2, 2)
print(f"Tú índice de masa corporal es de {IMC}kg/m². ")
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit.
gradoscelsius = float(input("Ingresa la temperatura en °C: "))
gradorfahrenheit = round(float((9/5) * gradoscelsius + 32), 2)
print(f"{gradoscelsius}°C equivalen a {gradorfahrenheit}°F. ")
# Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números.
print("Ingresemos tres números para calcular el promedio. ")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))
promedio = round((num1 + num2 + num3) / 3 , 2)
print(f"El promedio de los números propocionados es {promedio}. ")