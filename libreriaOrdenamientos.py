def ordenado (arreglo):
    longitud_arreglo=len(arreglo)
    for x in range(0, longitud_arreglo):
        for y in range(x+1, longitud_arreglo):
            if arreglo[x] > arreglo[y]: return False
    return True

arreglo=[3,1,1,1]
print(ordenado(arreglo))