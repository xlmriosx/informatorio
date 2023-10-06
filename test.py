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
