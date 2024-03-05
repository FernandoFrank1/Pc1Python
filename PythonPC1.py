#Variables:

# Problema 1: 
"""Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
usuario haya introducido."""

Nombre_Usuario = input('Ingrese su nombre de usuario: ')
print(f'¡Hola {Nombre_Usuario}!')


#Problema 2:
""""En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina."""

Consumo = float(input('¿Cuanto fue su consumo en el restaurante? $'))
Porcentaje_Propina = float(input('¿Que porcentaje de propina desea dejar al mesero? '))

Propina = Consumo * (Porcentaje_Propina / 100)

print(f'La cantidad de dinero a dejar como propina es: ${Propina}')


#Problema 3:
"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado."""

Peso_Payaso = 112 
Peso_Muñeca = 75 

Numero_Payasos = int(input('Ingresar la cantidad de payasos vendidos en el ultimo pedido: '))
Numero_Muñecas = int(input('Ingresar la cantidad de muñecas vendidas en el ultimo pedido: '))

Peso_Total = (Numero_Payasos*Peso_Payaso) + (Numero_Muñecas*Peso_Muñeca)

print(f'El peso total del paquete a enviar es de: {Peso_Total} g')


#Problema 4:
"""Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma: 1+2+3+...+n = n(n+1)/2"""

N = int(input('Ingrese un valor entero positivo: '))

Suma_Enteros = N * (N + 1) // 2

print(f'La suma de los {N} primeros enteros positivos desde 1 es: {Suma_Enteros}')


#Condicionales

#Problema 5:
"""Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows"""

Numero_shows = int(input('¿Cuántos shows musicales ha visto en el ultimo año? '))

if Numero_shows > 3:
    shows_vistos = True
else:
    shows_vistos = False

print(f'¿El usuario ha visto más de 3 shows musicales? {shows_vistos}')


#Problema 6:
"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10."""

Edad_Cliente = int(input('Ingrese su edad: '))

if Edad_Cliente < 4:
    print('Ingreso Gratis')
elif Edad_Cliente <= 4:
    print('Debe pagar $5')
elif Edad_Cliente <= 18:
    print('Debe pagar $5')
else:
    print('Debe pagar $10')


#Problema 7:
"""Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta"""

a = float(input('Ingrese un primer numero: '))
b = float(input('Ingrese un segundo numero: '))

print('¿Qué operación desea realizar?')
print('1. Sumar los dos números')
print('2. Restar el primero menos el segundo')
print('3. Multiplicar los dos números')

Opciones = input('Ingrese el número de la opción: ')

if Opciones == '1':
    print(f'La suma de {a} + {b} es {a+b}')
elif Opciones == '2':
    print(f'La resta de {a} - {b} es {a-b}')
elif Opciones == '3':
    print(f'La multiplicacion de {a} x {b} es {a*b}')
else:
    print('Ingrese una opcion correcta: Suma(1), Resta(2) o Multiplicacion(3)')


#Problema 8:
"""Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar"""

time = input('Ingrese la hora en formato HH:MM ')

hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

time_decimal = hours + (minutes / 60)

if 7.0 <= time_decimal <= 8.0:
    print('Es hora de desayunar')
elif 12.0 <= time_decimal <= 13.0:
    print('Es hora de almorzar')
elif 18.0 <= time_decimal <= 19.0:
    print('Es hora de cenar')


#Colecciones de Datos:

#Problema 9:
"""Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
'día', 'buen', 'Di']."""

#Primera opcion
lista_1 = ['Di', 'buen', 'día', 'a', 'papa']
lista_1.reverse()
print(lista_1)

#Segunda opcion
lista_2 = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista_2[::-1]
print(lista_invertida)


#Problema 10:
"""Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']"""

Colores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

Colores.remove(Colores[5])
Colores.remove(Colores[4])
Colores.remove(Colores[0])

print(Colores)


#Problema 11:
"""Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,, 5]"""

Numeros = [1, 1, 2, 3, 4, 4, 5, 1]

Numeros_Procesados = list(set(Numeros))
print(Numeros_Procesados)


#Problema 12:
"""Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip
Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.
Ejemplos:
Nombre Archivo: happy.jpg                  Salida Esperada: image/jpeg
Nombre Archivo: document.pdf               Salida Esperada: application/pdf"""

Extensiones_Mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

Nombre_Archivo = input('Ingrese el nombre del archivo: ')

Sufijo = Nombre_Archivo.lower().split('.')[-1]

Tipo_Mime = Extensiones_Mime.get(Sufijo, 'application/octet-stream')

print("Tipo MIME:", Tipo_Mime)