# Operandos normales
# Resta -
# Suma +
# Multiplicacion *
# Division /

# Operandos booleanos 
# and
# or
# igualdad ==
# comparativo >
# comparativo <

# Guarda archivo con CTRL + S

# Busqueda binaria

# Ejercicio guia - N 19
# Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. 
# Un número perfecto es aquel que es igual a la suma de sus divisores propios 
# (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

numero = int(input("Ingrese un numero: "))

divisores = []
suma = 0

for numero_menor in range(1,numero):
    if numero % numero_menor == 0:
        # print(f"{numero_menor} es divisor")
        # suma += numero_menor
        divisores.append(numero_menor)

# suma = sum(divisores)
for num in divisores:
    suma += num

if suma == numero:
    perfecto = True
else:
    perfecto = False


if perfecto:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")
