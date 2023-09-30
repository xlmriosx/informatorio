# crear una coleccion de facturas y sacar el promedio
# pedir al usuario primero la cantidad de facturas
# usar una lista para este ejercicio

facturas = []

numero_de_facturas = int(input("ingrese cantidad de facturas:"))

for num in range(1, numero_de_facturas+1):
    monto = int(input(f"ingrese monto de factura {num}: "))
    facturas.append(monto)

suma = sum(facturas)

promedio = suma / numero_de_facturas

print("El promedio de las facturas es: ",promedio)
