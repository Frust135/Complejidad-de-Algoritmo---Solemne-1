#-------------------------------------------------------------------
#__Algoritmo que retorna si un arreglo se encuentra ordenado o no__
#-------------------------------------------------------------------
def isOrdenado (arreglo):
    longitud_arreglo = len(arreglo)
    for x in range(0, longitud_arreglo):
        for y in range(x+1, longitud_arreglo):
            if arreglo[x] > arreglo[y]: return False #Compara uno por uno los datos con el fin de observar que esten todos ordenados, en caso de no haber un orden, retorna falso
    return True
#-------------------------------------------------------------------
#__Algoritmo de ordenamiento de Selección__
#-------------------------------------------------------------------
def sortSeleccion(arreglo):
    if isOrdenado(arreglo): return arreglo #En caso de que el algoritmo ya este ordenado, retorna el arreglo
    else:
        longitud_arreglo = len(arreglo)
        for x in range (0, longitud_arreglo-1):
            min_value = arreglo[x] #Se toma el elemento en la posición 0 como el elemento con el valor mínimo
            posicion = x #También se toma la posición de dicho elemento
            for y in range (x+1, longitud_arreglo):
                if arreglo[y]<min_value: 
                    min_value = arreglo[y] #Si existe un elemento con un valor menor al elemento de la posición inicial, este nuevo elemento pasa a ser el valor mínimo
                    posicion = y #De la mismo forma se registra la posición de dicho valor mínimo
            arreglo[posicion] = arreglo[x] #En la posición del valor mínimo se ingresa el valor correspondiente a x, que es mayor al valor mínimo
            arreglo[x] = min_value #Y en la posición de x, que es donde está el valor mayor al mínimo, se reemplaza con el valor mínimo
        return arreglo
#-------------------------------------------------------------------
#__Algoritmo de ordenamiento de Inserción__
#-------------------------------------------------------------------
def sortInsercion(arreglo):
    if isOrdenado(arreglo): return arreglo
    else:
        for recorrido in range (0, len(arreglo)):
            if arreglo[recorrido-1]>arreglo[recorrido]: #Revisa si el elemento ubicado a la izquierda del elemento analizado es mayor a él, de ser así, hay que ordenar
                for recorridoInsercion in range(0, recorrido): 
                    if arreglo[recorridoInsercion]>arreglo[recorrido]: #Se busca si existe un valor mayor a la izquierda de dicho elemento, para esto, se recorren todos los valores a la izquierda
                        aux = arreglo[recorridoInsercion] #En caso de ser así, se realiza un cambio de posición
                        arreglo[recorridoInsercion] = arreglo[recorrido]
                        arreglo[recorrido] = aux
                    else: #En caso de que no exista un elemento mayor más hacia allá a la izquierda, se realiza un cambio de posición con el elemento que se encuentra exactamente una posición a la izquierda
                        aux = arreglo[recorrido-1]
                        arreglo[recorrido-1] = arreglo[recorrido]
                        arreglo[recorrido] = aux
    return arreglo
#-------------------------------------------------------------------
#__Algoritmo de ordenamiento Burbuja__
#-------------------------------------------------------------------
def sortBurbuja(arreglo):
    if isOrdenado(arreglo): return arreglo
    else:
        for recorrido in range(len(arreglo)-1,0,-1): #Recorrimos el arreglo desde atrás hacia adelante
            for x in range (recorrido): #Y del mismo tiempo recorremos el arreglo desde principio hasta el elemento de la parte inferior que estamos analizando
                if arreglo[recorrido]<arreglo[x]: #En caso de que el elemento de más abajo, sea menor que uno de más arriba, el elemento de abajo sube
                    aux = arreglo[x]
                    arreglo[x] = arreglo[recorrido]
                    arreglo[recorrido] = aux #Y el elemento mayor, baja
    return arreglo

#-------------------------------------------------------------------
#__Algoritmo de ordenamiento QuickSort__
#-------------------------------------------------------------------
def quickSort(arreglo):
    if len(arreglo)<=1: return arreglo #Nuestro caso base corresponde a cuando la longitud del arreglo es menor a 1
    else:
        pivote = arreglo[0] #Seleccionamos un pivote, que en este caso como el arreglo esta desordenado, tomaremos el primer valor
        arreglo_mayores=[] #Consideramos un arreglo en donde irán los valores mayores al pivote, y en el otro los menores
        arreglo_menores=[]
        for recorrido in range (1, len(arreglo)): #Recorremos el arreglo desde 1, ya que el elemento 0 corresponde al pivote
            if arreglo[recorrido]>pivote: 
                arreglo_mayores.append(arreglo[recorrido]) #Si el elemento es mayor al pivote, lo almacenamos en el arreglo de mayores
            else:
                arreglo_menores.append(arreglo[recorrido]) #Si el elemento es menor al pivote, lo almacenamos en el arreglo de menores
        return quickSort(arreglo_menores) + [pivote] + quickSort(arreglo_mayores) #Concatemos lo que corresponde el arreglo de menores, el pivote, y el arreglo de menores en dicho orden, pero antes se realiza una llamada recursiva para ordenar el arreglo de menores y mayores, y así sucesivamente
#-------------------------------------------------------------------
#__Algoritmo de ordenamiento MergeSort__
#-------------------------------------------------------------------
def mergeSort(arreglo):
    if len(arreglo)<=1: return arreglo #De la misma forma que en el caso anterior, nuestro caso base es cuando la longitud del arreglo es menor a 1
    else:
       mitad = len(arreglo) //2 #Obtenemos la mitad de la longitud del arreglo
       mitad_izquierda=arreglo[mitad:] #Y en un arreglo almacenaremos los datos de la mitad izquierda
       mitad_derecha=arreglo[:mitad] #Y en otro arreglo almacenaremos los datos de la mitad derecha
       arreglo.clear() #Limpiamos nuestro arreglo, ya que ahí iremos ordenando nuestros datos de los arreglos de la mitad y derecha, de manera ordenada
       mergeSort(mitad_izquierda) #Realizamos una llamada recursiva, con el fin de ir separando los datos en arreglos de 1
       mergeSort(mitad_derecha) #Lo mismo con los datos de la mitad derecha
       while len(mitad_izquierda)>0 and len(mitad_derecha)>0: #Ahora se irán almacenando los datos en nuestro arreglo principal, para esto, el while se ejecutará siempre que hayan datos en la mitad izquierda y derecha
            if mitad_izquierda[0]<mitad_derecha[0]: #Si el dato de la mitad izquierda es menor
                arreglo.append(mitad_izquierda.pop(0)) #Dicho dato se almacenará dentro de nuestro arreglo, y ese dato será eliminado del arreglo de mitad izquierda
            else:
                arreglo.append(mitad_derecha.pop(0)) #Lo mismo en caso de que el dato de la mitad derecha sea menor 
       while len(mitad_izquierda)>0: #Finalmente si sobran datos en la mitad izquierda, se van agregando al final del arreglo, ya que se entiende que son los datos mayores del arreglo
           arreglo.append(mitad_izquierda.pop(0))
       while len(mitad_derecha)>0: #Lo mismo en caso que sobrasen datos en la mitad derecha, ya que se entiende que dichos elementos son los mayores del arreglo
           arreglo.append(mitad_derecha.pop(0) )
       return arreglo
#-------------------------------------------------------------------
#__ APARTADO DE PRUEBAS __
#-------------------------------------------------------------------
arregloSeleccion=[10,20,7,25,5,19,32,2]
arregloBurbuja=[10,20,7,25,5,19,32,2]
arregloInsercion=[10,20,7,25,5,19,32,2]
arregloQuickSort=[10,20,7,25,5,19,32,2]
arregloMergeSort=[10,20,7,25,5,19,32,2]
print("-----------------------------------------------------")
print("El resultado de sortSelección es:", sortSeleccion(arregloSeleccion))
print("-----------------------------------------------------")
print("El resultado de sortBurbuja es:",sortBurbuja(arregloBurbuja))
print("-----------------------------------------------------")
print("El resultado de sortInsercion es:",sortInsercion(arregloInsercion))
print("-----------------------------------------------------")
print("El resultado de quickSort es:", quickSort(arregloQuickSort))
print("-----------------------------------------------------")
print("El resultado de MergeSort es:", mergeSort(arregloMergeSort))
