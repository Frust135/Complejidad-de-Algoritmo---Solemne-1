from tkinter import *
from libreriaOrdenamientos import *
from timeit import default_timer
from numpy import arange, random
import matplotlib.pyplot as plt
#muestra los datos que se agregaron a la lista
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
    output = Opcion_metodo(StringIngreso) #Se realiza el ordenamiento del arreglo y se almacena en la variable output
    fin_timer = default_timer() #Una vez que se obtenga el output, es decir, que tengamos el arreglo ordenado, se toma otro timer, que corresponderá al tiempo final de ejecución del método de ordenamiento
    tiempo_ejecucion = fin_timer - inicio_timer #Se obtiene el tiempo de ejecución total del método de ordenamiento seleccionado
    Lista_numeros.insert(END,output) #Añade el arreglo de int al cuadro de texto

def Creacion_entrada():
    s=Seleccion.get()
    if s==1: #Si se selecciona la primer opción, habilita el primer entry (o input), y los otros 2 quedan deshabilitados
        User_entry1 = Entry(textvariable=ingreso_arreglo, state='normal') 
        User_entry2 = Entry(textvariable=ingreso_nulo, state='disabled')
        User_entry3 = Entry(state='disabled')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)
    if s==2: #En caso de seleccionar la segunda opción, los primeros 2 entrys o inputs, quedan habilitados
        User_entry1 = Entry(textvariable=cantidad_random, state='normal')
        User_entry2 = Entry(textvariable=limites, state='normal')
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

def Opcion_metodo(arreglo):
    s_m= Seleccion_metodo.get()
    if s_m==3: return sortSeleccion(arreglo) #Método Selección
    if s_m==4: return sortInsercion(arreglo) #Método Inserción
    if s_m==5: return sortBurbuja(arreglo) #Método Burbuja
    if s_m==6: return quickSort(arreglo) #Método QuickSort
    if s_m==7: return mergeSort(arreglo) #Método MergeSort
    if s_m==8: return heapSort(arreglo) #Método HeapSort

def generar_grafica(metodos, tiempos):
    y_pos = arange(len(metodos)) #Para generar el gráfico, necesitamos la longitud de variables en el eje Y
    plt.barh(y_pos, tiempos, color=(0.2, 0.4, 0.6, 0.6), height=0.4) #Con barh indicamos que será un gráfico de barras horizontal, en donde en el eje X, se ubicará el tiempo
    plt.yticks(y_pos,metodos) #Y en el eje Y se ubicarán los nombres de los métodos
    plt.show() #Finalmente se muestra el gráfico en pantalla
    

#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

mywindow=Tk()
mywindow.geometry("910x450")
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

box2=Label(bg="#b48471", width="35", height="21")
box2.place(x=320, y=100)


#Creación lista
Lista_numeros = Listbox(mywindow)
Lista_numeros.place(x=350, y=120)

#Creación de botón para guardar la información
Btn_ingresa = Button(mywindow, text="Ingresar", command= agregar_info)
Btn_ingresa.place(x=350, y=300)


#-------------------------------------------------------------------
#      Box 3
#-------------------------------------------------------------------
box3=Label(bg="#b48471", width="35", height="21")
box3.place(x=610, y=100)

metodos = ('Ordenamiento', 'Inserción', 'Burbuja')
tiempos = [10,20,5]
Btn_generarGrafico = Button(mywindow, text="Generar Gráfico", command=lambda: generar_grafica(metodos,tiempos))
Btn_generarGrafico.place(x=680, y=350)

mywindow.mainloop()
