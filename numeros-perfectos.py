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