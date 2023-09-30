# def es la sentencia que me indica una funcion
# funcion: ejecuta una serie de sentencias y devuelve un valor
# procedimiento: ejecuta una serie de sentencias y NO devuelve un valor

# EN PYTHON NO EXISTEN LOS PROCEDIMIENTOS. ES DECIR SOLO TENGO FUNCIONES EN PYTHON
def busqueda_binaria(lista, elemento): 
    '''
    Cuando le pase valores de variables para definir la funcion
    se van a llamar PARAMETROS, en este caso son lista y elemento
    '''
    izquierda = 0 
    derecha = len(lista) - 1  # [0,1,2,3]

    iteracion = 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"Iteracion: {iteracion}")
        print(f"Estoy parado en: {lista[medio]}")
        print(f"Lista: {lista[izquierda:derecha]}")
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
        iteracion += 1
    # muy similiar al break, pero hace que salga de la funcion
    return -1  # Elemento no encontrado

# Ejemplo de uso:
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = 3
resultado = busqueda_binaria(lista_ordenada, elemento_buscado) # Son ARGUMENTOS

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")
