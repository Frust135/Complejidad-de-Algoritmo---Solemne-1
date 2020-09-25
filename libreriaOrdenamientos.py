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

#__Algoritmo de ordenamiento Burbuja__
def sortBurbuja(arreglo):
    if isOrdenado(arreglo): return arreglo
    else:
        for recorrido in range(len(arreglo)-1,0,-1):
            for x in range (recorrido):
                if arreglo[recorrido]<arreglo[x]:
                    aux = arreglo[x]
                    arreglo[x] = arreglo[recorrido]
                    arreglo[recorrido] = aux
    return arreglo

#__ APARTADO DE PRUEBAS __
arreglo=[1,2,5,4,30,5,1,68,48,2,6]
print("-----------------------------------------------------")
print("El resultado de sortSelección es:", sortSeleccion(arreglo))
print("-----------------------------------------------------")
print("El resultado de sortBurbuja es:",sortBurbuja(arreglo))
print("-----------------------------------------------------")
