from tkinter import *
from libreriaOrdenamientos import *
from timeit import default_timer
from numpy import arange, random
import matplotlib.pyplot as plt
#-------------------------------------------------------------------
#      Obtiene los datos del menú, y retorna un arreglo en donde va el arreglo de números ordenado, 
#       y el tiempo demorado de la ejecución del método de ordenamiento
#-------------------------------------------------------------------
def agregar_info():
    s=Seleccion.get()
    if s==1: #Se indica que se seleccionó la primera opción, es decir, ingresar el arreglo a mano
        StringIngreso = ingreso_arreglo.get()   
        StringIngreso = StringIngreso.split(sep=',') #Separa el arreglo en partes
        StringIngreso = list(map(int,StringIngreso)) #Convierte el arreglo a Int
    if s==2:
        cantidad_valores = cantidad_random.get() #Obtiene la cantidad de valores del input "cantidad_random"
        cantidad_valores = cantidad_valores.split(sep=',') #Se hace un split, para tomar exclusivamente el primer valor
        cantidad_valores = int(cantidad_valores[0]) #Se selecciona el primer valor
        limites_random = limites.get() #Se realiza lo mismo con los limites inferiores y superiores
        limites_random = limites_random.split(sep=',')
        limite_inferior = int(limites_random[0])
        limite_superior = int(limites_random[1])
        arreglo_random = random.randint(limite_inferior,limite_superior,cantidad_valores) #Usando la librería random de numpy, se genera un arreglo con los limites inferiores y superiores, y con la cantidad de datos deseado
        StringIngreso = arreglo_random.tolist() #Convierte el array de Numpy, a un array común de Python
        User_entry3 = Entry(state='normal') #El arreglo es mostrado en pantalla en el entry 3
        User_entry3.place(x= 40, y=220)
        User_entry3.insert(0,StringIngreso)
    inicio_timer = default_timer() #Se inicializa un timer antes de ingresar al método de ordenamiento deseado
    print(inicio_timer)
    output = Opcion_metodo(StringIngreso) #Se realiza el ordenamiento del arreglo y se almacena en la variable output
    fin_timer = default_timer() #Una vez que se obtenga el output, es decir, que tengamos el arreglo ordenado, se toma otro timer, que corresponderá al tiempo final de ejecución del método de ordenamiento
    tiempo_ejecucion = fin_timer - inicio_timer #Se obtiene el tiempo de ejecución total del método de ordenamiento seleccionado
    arreglo_retorno=[output,tiempo_ejecucion]
    return arreglo_retorno
    #Lista_numeros.insert(END,output) #Añade el arreglo de int al cuadro de texto
#-------------------------------------------------------------------
#      Crea los input para ingresar datos, cuando se selecciona la opción de ingresar un número
#      Se habilita exclusivamente la primera barra para ingresar los datos
#      En caso de seleccionar la opción Random, se habilitan las 2 barras, la primera para 
#      Ingresar la cantidad de datos, y la segunda para ingresar el rango
#-------------------------------------------------------------------
def Creacion_entrada():
    s=Seleccion.get()
    if s==1: #Si se selecciona la primer opción, habilita el primer entry (o input), y los otros 2 quedan deshabilitados
        User_entry1 = Entry(textvariable=ingreso_arreglo, state='normal') 
        User_entry1.insert(0,"1,2,3,4")
        User_entry2 = Entry(textvariable=ingreso_nulo, state='disabled')
        User_entry3 = Entry(state='disabled')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)
    if s==2: #En caso de seleccionar la segunda opción, los primeros 2 entrys o inputs, quedan habilitados
        User_entry1 = Entry(textvariable=cantidad_random, state='normal')
        User_entry1.insert("0","5")
        User_entry2 = Entry(textvariable=limites, state='normal')
        User_entry2.insert("0","1,100")
        User_entry3 = Entry (state='disabled')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)
    if s!=1 and s!=2: #En caso que no se haya seleccionado ninguna opción, todos los entry o inputs se mantienen deshabilitados
        User_entry1 = Entry(textvariable=ingreso_nulo, state='disabled')
        User_entry2 = Entry(textvariable=ingreso_nulo, state='disabled')
        User_entry3 = Entry(state='disabled')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)
#-------------------------------------------------------------------
#      Retorna el método de ordenamiento seleccionado
#-------------------------------------------------------------------
def Opcion_metodo(arreglo):
    s_m= Seleccion_metodo.get()
    if s_m==3: return sortSeleccion(arreglo) #Método Selección
    if s_m==4: return sortInsercion(arreglo) #Método Inserción
    if s_m==5: return sortBurbuja(arreglo) #Método Burbuja
    if s_m==6: return quickSort(arreglo) #Método QuickSort
    if s_m==7: return mergeSort(arreglo) #Método MergeSort
    if s_m==8: return heapSort(arreglo) #Método HeapSort
#-------------------------------------------------------------------
#      Genera la gráfica en función de un arreglo de métodos (Nombres), y un arreglo de tiempos (Tiempo de ejecución)
#-------------------------------------------------------------------
def generar_grafica(metodos, tiempos): 
    y_pos = arange(len(metodos)) #Para generar el gráfico, necesitamos la longitud de variables en el eje Y
    plt.barh(y_pos, tiempos, color=(0.2, 0.4, 0.6, 0.6), height=0.4) #Con barh indicamos que será un gráfico de barras horizontal, en donde en el eje X, se ubicará el tiempo
    plt.yticks(y_pos,metodos) #Y en el eje Y se ubicarán los nombres de los métodos
    plt.title("Métodos y Tiempo")
    plt.show() #Finalmente se muestra el gráfico en pantalla
#-------------------------------------------------------------------
#      Obtienen la información de la columna nombres y tiempos, y las almacenan en un arreglo
#      Para luego ejecutar la función de genear gráficas entregando dichos arreglos
#-------------------------------------------------------------------
def obtener_data():
    metodos =[] #Definimos el arreglo métodos, que es donde se irán almacenando los nombres de los métodos
    tiempos =[] #Y en el arreglo tiempo, iremos agregando el tiempo que se demora cada algoritmo de ordenamiento
#Almacenamos en una variable Tiempo lo que se encuentre en la columna 2 de cada fila, esto es aplicado con cada uno de los métodos de ordenamiento
    seleccionTiempo=tabla.grid_slaves(row=1, column=2)[0] 
    insercionTiempo=tabla.grid_slaves(row=2, column=2)[0] 
    burbujaTiempo=tabla.grid_slaves(row=3, column=2)[0]
    quicksortTiempo=tabla.grid_slaves(row=4, column=2)[0]
    mergesortTiempo=tabla.grid_slaves(row=5, column=2)[0]
    heapsortTiempo=tabla.grid_slaves(row=6, column=2)[0]
    if (isinstance(seleccionTiempo.cget("text"),float)==True): #Revisamos si la variable corresponde a un float, es decir, corresponde a un valor con la estructura de tiempo
        tiempos.append(seleccionTiempo.cget("text")) #De ser así, este valor lo ingresamos dentro de nuestro arreglo tiempo
        seleccionNombre=tabla.grid_slaves(row=1, column=0)[0] #Obtenemos también el nombre de dicho método de ordenamiento
        metodos.append(seleccionNombre.cget("text")) #Y lo ingresamos en el arreglo de métodos
#Esto lo aplicamos con cada uno de los métodos existentes
    if (isinstance(insercionTiempo.cget("text"),float)==True):
        tiempos.append(insercionTiempo.cget("text"))
        insercionNombre=tabla.grid_slaves(row=2, column=0)[0]
        metodos.append(insercionNombre.cget("text"))
    if (isinstance(burbujaTiempo.cget("text"),float)==True):
        tiempos.append(burbujaTiempo.cget("text"))
        burbujaNombre=tabla.grid_slaves(row=3, column=0)[0]
        metodos.append(burbujaNombre.cget("text"))
    if (isinstance(quicksortTiempo.cget("text"),float)==True):
        tiempos.append(quicksortTiempo.cget("text"))
        quicksortNombre=tabla.grid_slaves(row=4, column=0)[0]
        metodos.append(quicksortNombre.cget("text"))
    if (isinstance(mergesortTiempo.cget("text"),float)==True):
        tiempos.append(mergesortTiempo.cget("text"))
        mergesortNombre=tabla.grid_slaves(row=5, column=0)[0]
        metodos.append(mergesortNombre.cget("text"))
    if (isinstance(heapsortTiempo.cget("text"),float)==True):
        tiempos.append(heapsortTiempo.cget("text"))
        heapsortNombre=tabla.grid_slaves(row=6, column=0)[0]
        metodos.append(heapsortNombre.cget("text"))
#Finalmente con nuestros arreglos de métodos y tiempos, continuamos a genera el gráfico y mostrarlo en pantalla    
    generar_grafica(metodos,tiempos)
#-------------------------------------------------------------------
#      Crea (O mejor dicho) modifica las columnas de la talba para escribir el arreglo ordenado, y el tiempo de 
#      ejecución de dicho algoritmo ede ordenamiento
#-------------------------------------------------------------------    
def crear_columna():
    s_m=Seleccion_metodo.get() #Obtiene la información de que método fue seleccionado
    info=agregar_info() #Genera la información, es decir, el arreglo ordenado y el tiempo de ejecución
    arreglo=info[0] #El arreglo es lamacenado dentro de la variable arreglo
    tiempo=info[1] #Y el tiempo es agregado a la variable tiempo
    if s_m==3: #Método Selección
        seleccion=tabla.grid_slaves(row=1, column=1)[0] #Se selecciona la columna de arreglo
        seleccion.config(text=arreglo) #E inserta (O mejor dicho, módifica) en la columna arreglo, el arreglo obtenido 
        seleccion=tabla.grid_slaves(row=1, column=2)[0] #Lo mismo con el tiempo, se selecciona la variable tiempo
        seleccion.config(text=tiempo) #Y se inserta. Esto se repite con cada uno de los métodos de ordenamiento
    if s_m==4: #Método Inserción
        insercion=tabla.grid_slaves(row=2, column=1)[0]
        insercion.config(text=arreglo)
        insercion=tabla.grid_slaves(row=2, column=2)[0]
        insercion.config(text=tiempo)
    if s_m==5: #Método Burbuja
        burbuja=tabla.grid_slaves(row=3, column=1)[0]
        burbuja.config(text=arreglo)
        burbuja=tabla.grid_slaves(row=3, column=2)[0]
        burbuja.config(text=tiempo)
    if s_m==6: #Método QuickSort
        quicksort=tabla.grid_slaves(row=4, column=1)[0]
        quicksort.config(text=arreglo)
        quicksort=tabla.grid_slaves(row=4, column=2)[0]
        quicksort.config(text=tiempo)
    if s_m==7: #Método MergeSort
        mergesort=tabla.grid_slaves(row=5, column=1)[0]
        mergesort.config(text=arreglo)
        mergesort=tabla.grid_slaves(row=5, column=2)[0]
        mergesort.config(text=tiempo)
    if s_m==8: #Método HeapSort 
        heapsort=tabla.grid_slaves(row=6, column=1)[0]
        heapsort.config(text=arreglo)
        heapsort=tabla.grid_slaves(row=6, column=2)[0]
        heapsort.config(text=tiempo)
#-------------------------------------------------------------------
#      Botón de limpiar tabla
#-------------------------------------------------------------------
def clean_tabla():
    tiempo='                           Tiempo                           '
    arreglo='                                                                                 Arreglo                                                                                 '
    #Al igual que en los métodos anteriores, almacenamos el tiempo de cada fila en distintas variables
    seleccionTiempo=tabla.grid_slaves(row=1, column=2)[0] 
    insercionTiempo=tabla.grid_slaves(row=2, column=2)[0] 
    burbujaTiempo=tabla.grid_slaves(row=3, column=2)[0]
    quicksortTiempo=tabla.grid_slaves(row=4, column=2)[0]
    mergesortTiempo=tabla.grid_slaves(row=5, column=2)[0]
    heapsortTiempo=tabla.grid_slaves(row=6, column=2)[0]
    #Y configuramos su texto por la variable 'Tiempo'
    seleccionTiempo.config(text=tiempo) 
    insercionTiempo.config(text=tiempo)
    burbujaTiempo.config(text=tiempo)
    quicksortTiempo.config(text=tiempo)
    mergesortTiempo.config(text=tiempo)
    heapsortTiempo.config(text=tiempo)
    #Lo mismo para los arreglos
    seleccionArreglo=tabla.grid_slaves(row=1, column=1)[0] 
    insercionArreglo=tabla.grid_slaves(row=2, column=1)[0] 
    burbujaArreglo=tabla.grid_slaves(row=3, column=1)[0]
    quicksortArreglo=tabla.grid_slaves(row=4, column=1)[0]
    mergesortArreglo=tabla.grid_slaves(row=5, column=1)[0]
    heapsortArreglo=tabla.grid_slaves(row=6, column=1)[0]
    #Se configura su texto por la variable 'Arreglo'
    seleccionArreglo.config(text=arreglo) 
    insercionArreglo.config(text=arreglo)
    burbujaArreglo.config(text=arreglo)
    quicksortArreglo.config(text=arreglo)
    mergesortArreglo.config(text=arreglo)
    heapsortArreglo.config(text=arreglo)
#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

mywindow=Tk()
mywindow.geometry("1270x450")
mywindow.title("Metodos de búsqueda")
mywindow['bg'] = '#72382e'

Titulo=Label(text="Métodos de ordenamiento" ,font=("Cambria",15),fg="#210e0c" , bg="#e4ba9f", width="893", height="3")

Titulo.pack()

#-------------------------------------------------------------------
#      Ingreso de datos
#-------------------------------------------------------------------

box1=Label(bg="#b48471", width="35", height="21")
box1.place(x=25, y=100)

Ingreso_label = Label(text="Ingrese la opción", bg="#b48471", font=("Cambria",13), fg="#210e0c")
Ingreso_label.place(x=29, y=100)

Seleccion = IntVar()

rdioNumeros = Radiobutton(mywindow, text="Ingresar números",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=1, command=Creacion_entrada)
rdioNumeros.place(x=25, y=130)

rdioRandom = Radiobutton(mywindow, text="Ingresar números random",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=2, command=Creacion_entrada)
rdioRandom.place(x=25, y=150)

#-------------------------------------------------------------------
#      Selección de método de ordenamiento
#-------------------------------------------------------------------
Ing_met = Label(text="Ingrese el método de", bg="#b48471", font=("Cambria",13), fg="#210e0c")
Ing_met2 = Label(text="ordenamiento", bg="#b48471", font=("Cambria",13), fg="#210e0c")
Ing_met.place(x=29, y=240)
Ing_met2.place(x=29, y=263)

Seleccion_metodo= IntVar()
rdioSeleccion = Radiobutton(mywindow, text="Selección",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion_metodo, value=3)
rdioSeleccion.place(x=25, y=285)

rdioInsercion = Radiobutton(mywindow, text="Inserción",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion_metodo, value=4)
rdioInsercion.place(x=25, y=305)

rdioBurbuja = Radiobutton(mywindow, text="Burbuja",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion_metodo, value=5)
rdioBurbuja.place(x=25, y=325)

rdioQuicksort = Radiobutton(mywindow, text="Quicksort",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion_metodo, value=6)
rdioQuicksort.place(x=25, y=345)

rdioMergesort = Radiobutton(mywindow, text="Mergesort",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion_metodo, value=7)
rdioMergesort.place(x=25, y=365)

rdioHeapsort = Radiobutton(mywindow, text="Heapsort",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion_metodo, value=8)
rdioHeapsort.place(x=25, y=386)

#-------------------------------------------------------------------
#     Box 2
#-------------------------------------------------------------------
#Variables para los inputs
ingreso_arreglo = StringVar()
ingreso_nulo = StringVar()
cantidad_random = StringVar()
limites = StringVar()
valores_generados = StringVar()
Creacion_entrada()

box2=Label(bg="#b48471", width="130", height="21")
box2.place(x=320, y=100)


#Creación de botón para guardar la información
Btn_ingresa = Button(mywindow, text="Ingresar", command= lambda:crear_columna()) #Este botón crea (O mejor dicho módifica) una columna
Btn_ingresa.place(x=650, y=365)


#-------------------------------------------------------------------
#     TABLA
#-------------------------------------------------------------------
tabla=Label(bg="#b48471", width="80", height="21")
tabla.place(x=340,y=130)
texto = ['          Método          ', '                                                                                 Arreglo                                                                                 ', '                           Tiempo                           ']
#Se genera la tabla
for fila in range(7):
    for columna in range(3):
        label=Label(tabla, text=texto[columna], bg="white", fg="black")
        label.grid(row=fila, column=columna,sticky="nsew", padx=1,pady=4)
        box2.grid_columnconfigure(columna, weight=1)
#Se selecciona cada fila correspondiente a su método de ordenamiento, y la columna 0 correspondiente al nombre
seleccion=tabla.grid_slaves(row=1, column=0)[0]
insercion=tabla.grid_slaves(row=2, column=0)[0]
burbuja=tabla.grid_slaves(row=3, column=0)[0]
quicksort=tabla.grid_slaves(row=4, column=0)[0]
mergesort=tabla.grid_slaves(row=5, column=0)[0]
heapsort=tabla.grid_slaves(row=6, column=0)[0]
#Y se cambia el nombre de cada una de las columnas por sus respectivos nombres
seleccion.config(text="Selección")
insercion.config(text="Inserción")
burbuja.config(text="Burbuja")
quicksort.config(text="QuickSort")
mergesort.config(text="MergeSort")
heapsort.config(text="HeapSort")
#-------------------------------------------------------------------
#     GRÁFICO
#-------------------------------------------------------------------

Btn_generarGrafico = Button(mywindow, text="Generar Gráfico", command=lambda: obtener_data()) #Este botón ejecuta la función obtener Data, que obtiene la información de las columnas, y genera el gráfico
Btn_generarGrafico.place(x=720, y=365)
#-------------------------------------------------------------------
#     Botón para limpiar
#-------------------------------------------------------------------

Btn_limpiar = Button(mywindow, text="Limpiar Tabla", command=lambda: clean_tabla())
Btn_limpiar.place(x=830,y=365)
#-------------------------------------------------------------------
#     Loop de la ventana
#-------------------------------------------------------------------
mywindow.mainloop()
