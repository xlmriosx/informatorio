# Si no especifico nada en una funcion que devuelve?

Respuesta: None

# Se corre la funcion cuando la defino?

```
# main.py --> python main.py
def algo():
    return 1

```

Respuesta: Si no la invoco no se va a ejecutar la funcion

# Como invoco a una funcion?

Respuesta:
```
# main.py --> python main.py
def algo():
    return 1

algo() # invoco a la funcion
```

# Como ejecuto la siguiente funcion?

```
# main.py --> python main.py
def hi(name):
    print(f"Hi {name}")
    
hi("Lucas")

```

# Asignacion de valores por default
```
def default(var1=10, var2=20):
    return var1, var2

# Python va a tomar como que var1 es 10 y var2 es 20, cuando NO le paso un valor para ese parametro
```

# Asignacion de valores por default
```
def default(var1=10, var2=20):
    return var1, var2

# Python va a tomar como que var1 es 10 y var2 es 20, cuando NO le paso un valor para ese parametro
```

# Argumentos indeterminados por posicion
```
def suma(*args):
    print(type(args))
    s = 0
    for arg in args:
        s += arg
    return s

suma(1, 3, 4, 2, 5, 6, 7, 8)
#Salida 10

suma(1, 1)
#Salida 2
```

# Argumentos indeterminados por nombre
```
def suma(**expedientes):
    for nombre, apellido in expedientes.items():
        print("Nombre:", nombre)
        print("Apellido:", apellido)
    
suma(Lucas="Rios", Leo="Reichert")
```


# usando todo el chiche
```
def default(var1, var2=10, *args, **kwargs):
    '''
        DOCUMENTACION DEL FUNCION DEL CODIGO
        var1
        var2
        args
        kwargs
    '''
    print("var1:",var1)
    print("default:",var2)
    print("indeterminados por posicion:",args)
    print("indeterminados por nombre:",kwargs)

default(var1=2)
```