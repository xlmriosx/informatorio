# Ejercicio 1
Resultados posibles en operaciones booleanas 1 y 0
res = 0 + 1 + 0 + 1
res = 1 + 1 ==> 1
```
res = False + True + False + True
res = True + True ==> True
```
# Ejercicio 2
Resultados posibles en operaciones booleanas 1 y 0
```
res = False * True * False * True
res = False
```
# Ejercicio 3
```
res = False + True + False + True
res = True + True ==> 
```
# Ejercicio 4
```
res = False * True * False * True
res = False
```
# Ejercicio 5
```
x = 5
y = 20
z = x + y
print(z + 8) --> 33
print(z) --> 25
```
# Ejercicio 6.1
Que es el tipado?
type

string --> 'algo' "algo" """algo""" '''algo'''

integer(enteros) --> 1 2 3 4 5 

float(racionales/decimales) --> 10.2 3.141521 2.32

tuplas --> (1,2,3) (1) (3.123, 3) ## Es ordenado, inmutable

set --> {1, 3, 2, 'hola', 'como', (12), 1} ## Es desordenado, mutable, no pueden tener elementos iguales

listas --> [1, 2, 3, "hola", 'maradona'] ## Es ordenada, mutable, puede tener cosas repetidas

dicccionario --> {} # Es del tipo llave:valor, key:value; es desordenado, mutable
diccionario = {1:"uno", 2:"dos", 3:"tres", '100':"cien", 0:'cero'}

# Ejercicio 6.2
Que es un lenguaje de tipado dinaminico?
```
# app.js --> Aplicacion javascript
let var1 = ...
const var2 = ...
```

```
# pepito.py --> Aplicacion python
numero1 = "Messi"
numero2 = 2
numero3 = "2"
```
Respuesta: 
- Es un lenguaje que toma por defecto el tipo de variables en funcion a lo que ingresemos
- Significa que las variables toman el mismo tipo de dato que el valor que contienen.
- Es que se puede definir dinamicamente osea que no hace falta definir que es solo toma el tipoo de variable

# Ejercicio 7
Cuando se definen los tipos de las variables?

Tiempos:
- En construccion
- En compilacion
- En despliegue
- En ejecucion

Respuesta: En ejecucion

# Ejercicio 8
```
variable_a = "45"
variable_b = 3
resultado = variable_a * variable_b
print(resultado)
```

Respuesta: '454545'

# Ejercicio 9
>Que es una palabra reservada?

if, exit, else, print, while, True, False, continue, for, etc

>Que no puedo hacer con las palabras reservadas?

Usarlos como variables

if =
else = 

# Ejercicio 10
Como se ejecuta un programa en python por consola?
```
python test.py --> Por defecto
py test.py --> Se debe configurar
python "test.py" --> No se ejecuta
```

# Ejercicio 11
Se puede cambiar de tipos de datos en python?
```
numero = "10"
print(type(numero))
numero = 10
print(type(numero))
numero = "10"
print(type(numero))
numero = int(numero)
print(type(numero))
numero = float(numero)
print(type(numero))
```
Respuesta: Si, se puede cambiar de tipo de dato

# Ejercicio 12
Que es el orden de procedencia? Identificar los ordenes de los operandos

Es aquello que me indica que operacion se realizara primero

Menor ---> mayor

and, or, +, -, *, /, //, %, **

# Ejercicio 13
Que es PEP8?
- Nombre de las variabes sin espacio
- Los nombre de las variables que son constantes como se escriben? --> MAYUSCULAS

```
PI = 3.14152123
MESSI = 10
ACELERACION_GRAVEDAD_TIERRA = 9.81 # -- Utilizar _ para separar palabras
```

# Ejercicio 14
Que es case sensitive?
No es lo mismo decir: dos_tazas_de_te <> DOS_TAZAS_DE_TE
