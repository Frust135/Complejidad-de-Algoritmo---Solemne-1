#__Algoritmo que retorna si un arreglo se encuentra ordenado o no__
def isOrdenado (arreglo):
    longitud_arreglo = len(arreglo)
    for x in range(0, longitud_arreglo):
        for y in range(x+1, longitud_arreglo):
            if arreglo[x] > arreglo[y]: return False
    return True

#__Algoritmo de ordenamiento de Selección__
def sortSeleccion(arreglo):
    if isOrdenado(arreglo): return arreglo
    else:
        longitud_arreglo = len(arreglo)
        for x in range (0, longitud_arreglo-1):
            min_value = arreglo[x]
            posicion = x
            for y in range (x+1, longitud_arreglo):
                if arreglo[y]<min_value: 
                    min_value = arreglo[y]
                    posicion = y
            arreglo[posicion] = arreglo[x]
            arreglo[x] = min_value
        return arreglo

#Algoritmo de busqueda: burbuja.
def burbuja(arreglo):
    a=1
    return a