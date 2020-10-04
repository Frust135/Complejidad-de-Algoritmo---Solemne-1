#-------------------------------------------------------------------
#      Algoritmo que retorna si un arreglo se encuentra ordenado o no
#-------------------------------------------------------------------
def isOrdenado (arreglo):
    longitud_arreglo = len(arreglo)
    for x in range(0, longitud_arreglo):
        for y in range(x+1, longitud_arreglo):
            if arreglo[x] > arreglo[y]: return False #Compara uno por uno los datos con el fin de observar que esten todos ordenados, en caso de no haber un orden, retorna falso
    return True
#-------------------------------------------------------------------
#      Algoritmo de ordenamiento de Selección
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
#      Algoritmo de ordenamiento de Inserción
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
#      Algoritmo de ordenamiento Burbuja
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
#      Algoritmo de ordenamiento QuickSort
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
#      Algoritmo de ordenamiento MergeSort
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
#      Algoritmo de ordenamiento HeapSort
#-------------------------------------------------------------------
#Comprender que este algoritmo genera un  Heap (un árbol binario), en el cual, se comparan los hijos con cada padre para ver cual es mayor
#Y una vez que exista un orden, se continua a reemplazar la raíz, y siendo la raíz el dato más grande, se almacena al final del arreglo.

#      Algoritmo HeapSort
def heapSort(arreglo):
    longitud = len(arreglo)
    mitad_longitud = longitud//2
    for recorrido in range(mitad_longitud-1, -1, -1): #Empezamos en la mitad del arreglo-1, ya que ahí se encontrará la primera raíz, o nodo padre
        generarHeap(arreglo, longitud, recorrido) #Generamos el Heap de máximos del arreglo
    for recorrido in range(longitud-1, 0, -1): #Una vez realizado el Heap, continuamos a extraer los elementos, cambiando sus posiciones con la raíz
        aux = arreglo[recorrido]
        arreglo[recorrido] = arreglo[0]
        arreglo[0] = aux #Recordar que siempre vamos a ir removiendo la raíz, y reemplazandola por el hijo mayor
        generarHeap(arreglo, recorrido, 0) #Y se realiza otro Heap
    return arreglo

#      Algoritmo que genera el Heap (árbol binario)

def generarHeap(arreglo, longitud_heap, longitud_final):
    elemento_mayor = longitud_final
    hIzq = 2*elemento_mayor+1 #Dentro del Heap, empezamos indicando las posiciones del hijo izquierdo
    hDer = 2*elemento_mayor+2 #Y también del hijo derecho
    if hIzq<longitud_heap and arreglo[longitud_final]<arreglo[hIzq]: #Comparamos si existe un hijo izquierdo, y si es mayor que la raíz
        elemento_mayor = hIzq #De ser así, este será el valor del parámetro más grande
    if hDer<longitud_heap and arreglo[elemento_mayor]<arreglo[hDer]: #De la misma forma, si el hijo izquierdo no existe, o es menor que la raíz, continuamos con el hijo derecho
        elemento_mayor = hDer
    if elemento_mayor != longitud_final: #En caso de que los hijos sean menores que la raíz, se coninua a reemplazar la raíz con el elemento que corresponda al elemento mayor, o en caso contrario, con el que se encuentre más a la derecha de los hijos
        aux = arreglo[longitud_final]
        arreglo[longitud_final] = arreglo[elemento_mayor]
        arreglo[elemento_mayor] = aux 
        generarHeap(arreglo, longitud_heap,elemento_mayor) #Se realiza el cambio, y se realiza otro Heap
