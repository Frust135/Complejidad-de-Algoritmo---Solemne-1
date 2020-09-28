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

#__Algoritmo de ordenamiento de Inserción__
def sortInsercion(arreglo):
    if isOrdenado(arreglo): return arreglo
    else:
        for recorrido in range (0, len(arreglo)):
            if arreglo[recorrido-1]>arreglo[recorrido]:
                for recorridoInsercion in range(0, recorrido):
                    if arreglo[recorridoInsercion]>arreglo[recorrido]:
                        aux = arreglo[recorridoInsercion]
                        arreglo[recorridoInsercion] = arreglo[recorrido]
                        arreglo[recorrido] = aux
                    else:
                        aux = arreglo[recorrido-1]
                        arreglo[recorrido-1] = arreglo[recorrido]
                        arreglo[recorrido] = aux
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
#__Algoritmo de ordenamiento QuickSort__
def quickSort(arreglo):
    if len(arreglo)<=1: return arreglo
    else:
        pivote = arreglo[0]
        arreglo_mayores=[]
        arreglo_menores=[]
        for recorrido in range (1, len(arreglo)):
            if arreglo[recorrido]>pivote: 
                arreglo_mayores.append(arreglo[recorrido])
            else:
                arreglo_menores.append(arreglo[recorrido])
        return quickSort(arreglo_menores) + [pivote] + quickSort(arreglo_mayores)


#__ APARTADO DE PRUEBAS __
arregloSeleccion=[10,20,7,25,5,19,32,2]
arregloBurbuja=[10,20,7,25,5,19,32,2]
arregloInsercion=[10,20,7,25,5,19,32,2]
arregloQuickSort=[10,20,7,25,5,19,32,2]
print("-----------------------------------------------------")
print("El resultado de sortSelección es:", sortSeleccion(arregloSeleccion))
print("-----------------------------------------------------")
print("El resultado de sortBurbuja es:",sortBurbuja(arregloBurbuja))
print("-----------------------------------------------------")
print("El resultado de sortInsercion es:",sortInsercion(arregloInsercion))
print("-----------------------------------------------------")
print("El resultado de quickSort es:", quickSort(arregloQuickSort))