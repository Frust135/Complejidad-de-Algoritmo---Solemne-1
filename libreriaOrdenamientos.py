#__Algoritmo que retorna si un arreglo se encuentra ordenado o no__
def isOrdenado (arreglo):
    longitud_arreglo=len(arreglo)
    for x in range(0, longitud_arreglo):
        for y in range(x+1, longitud_arreglo):
            if arreglo[x] > arreglo[y]: return False
    return True
#__Algoritmo de Selección__
def sortSeleccion(arreglo):
    if isOrdenado(arreglo): return arreglo
    
