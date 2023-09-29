# Pregunta 1
Que estructura de control iterativa es util para recorrer una lista?
- for
- while

Respusta: for

# Pregunta 2
l_a = ['k','h',4]
l_b = ['a','b',2]
l_c = l_a

l_a.extend(l_b)
print(l_a)

- ['k','h',4]['a','b',2] 
- ['k','h',4, ['a','b',2]]
- ['k','h',4,'a','b',2]

Respuesta: 3

# Pregunta 3
Que hace el len() ?

Respuesta: Te devuelve la cantida de elementos de un objeto iterable

# Pregunta 4
class dict: no ordenado, se accede por la llave (no puede tener dos llaves iguales porque son unicas), mutable

# Pregunta 5 
shuffle()

Respuesta:

# Ejercicio 1
```
lista = []

for i in range(1,20):
    numero = random.randint(1, 10000)
    lista.append(numero)

print(lista)

var_min = 10001
var_max = 0

for numero in lista:
    if numero > var_max:
        var_max = numero
    if numero < var_min:
        var_min = numero

print(f"El número mayor es: {var_max}")
print(f"El número menor es: {var_min}")
```

# Generador de lista aleatoria

```
import random

# [1,2,3,4,5,6] -> var[-1]

# [9,2,1,5,10] -> var_max = -10000

# Inicializamos variable
lista = []

for i in range(1,20):
    numero = random.randint(1, 10000)
    lista.append(numero)

#lista.append(777)
lista.sort()
print(lista)
```

# Ejercicio 2
```
# Algoritmo de busqueda lineal
# [1,2,3,990,5000,10000]
# [9,2,1,5,10]

buscar = 777
vuelta = 0

for numero in lista:
    vuelta += 1
    if buscar == numero:
        print(f"El valor {buscar} existe")
        break

    if numero > buscar:
        print(f"No se encontro el valor {buscar} salimos del bucle cuando encontro {numero}")
        break

print(f"cantidad de vueltas: {vuelta}")
print("Salimos del bucle")
```

# Ejercicio 3
```
for numero in lista:
    vueltas += 1
    if buscar == numero:
        encontro = True
        break
    
if encontro:
    print(f"Se encontro el valor {buscar}")
else:
    print(f"No se encontro el valor {buscar}")

print(f"Se dieron {vueltas} vueltas")
```