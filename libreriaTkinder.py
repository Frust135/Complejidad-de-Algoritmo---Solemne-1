from tkinter import *
from libreriaOrdenamientos import *
#muestra los datos que se agregaron a la lista
def enviar_info():
    User_ingreso = Ingreso.get()
    
    print(User_ingreso)

def agregar_info():
    StringIngreso = Ingreso.get()
    StringIngreso = StringIngreso.split(sep=',') #Separa el arreglo en partes
    StringIngreso = list(map(int,StringIngreso)) #Convierte el arreglo a Int
    Lista_numeros.insert(END,StringIngreso) #Añade el arreglo de int al cuadro de texto
    print(StringIngreso)

def Creacion_entrada():
    s=Seleccion.get()
    if s==1:
        User_entry1 = Entry(textvariable=Ingreso, state='normal')
        User_entry2 = Entry(textvariable=Ingreso, state='disabled')
        User_entry3 = Entry(textvariable=Ingreso, state='disabled')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)
    if s==2:
        User_entry1 = Entry(textvariable=Ingreso, state='normal')
        User_entry2 = Entry(textvariable=Ingreso, state='normal')
        User_entry3 = Entry(textvariable=Ingreso, state='normal')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)
    if s!=1 and s!=2:
        User_entry1 = Entry(textvariable=Ingreso, state='disabled')
        User_entry2 = Entry(textvariable=Ingreso, state='disabled')
        User_entry3 = Entry(textvariable=Ingreso, state='disabled')
        User_entry1.place(x= 40, y=180)
        User_entry2.place(x= 40, y=200)
        User_entry3.place(x= 40, y=220)

def Opcion_metodo(arreglo):
    s_m= Seleccion_metodo.get()
    if s_m==3:
        sortSeleccion(arreglo)
    if s_m==4:
        sortInsercion(arreglo)
    if s_m==5:
        sortBurbuja(arreglo)
    if s_m==6:
        quickSort(arreglo)
    if s_m==7:
        mergeSort(arreglo)
    if s_m==8:
        heapSort(arreglo)

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
#      Seleccion de metodo de ordenamiento
#-------------------------------------------------------------------
Ing_met = Label(text="Ingrese el método de", bg="#b48471", font=("Cambria",13), fg="#210e0c")
Ing_met2 = Label(text="ordenamiento", bg="#b48471", font=("Cambria",13), fg="#210e0c")
Ing_met.place(x=29, y=240)
Ing_met2.place(x=29, y=263)

Seleccion_metodo= IntVar()

rdioSeleccion = Radiobutton(mywindow, text="Selección",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=3, command=Opcion_metodo)
rdioSeleccion.place(x=25, y=285)

rdioInsercion = Radiobutton(mywindow, text="Inserción",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=4, command=Opcion_metodo)
rdioInsercion.place(x=25, y=305)

rdioBurbuja = Radiobutton(mywindow, text="Burbuja",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=5, command=Opcion_metodo)
rdioBurbuja.place(x=25, y=325)

rdioQuicksort = Radiobutton(mywindow, text="Quicksort",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=6, command=Opcion_metodo)
rdioQuicksort.place(x=25, y=345)

rdioMergesort = Radiobutton(mywindow, text="Mergesort",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=7, command=Opcion_metodo)
rdioMergesort.place(x=25, y=365)

rdioHeapsort = Radiobutton(mywindow, text="Heapsort",bg="#b48471",fg="#210e0c",font=("Cambria",11),variable=Seleccion, value=8, command=Opcion_metodo)
rdioHeapsort.place(x=25, y=386)

#-------------------------------------------------------------------
#     Box 2
#-------------------------------------------------------------------
Ingreso = StringVar()
Creacion_entrada()

box2=Label(bg="#b48471", width="35", height="21")
box2.place(x=320, y=100)

User_entry = Entry(textvariable=Ingreso)
User_entry.place(x= 180, y=200)

#creacion lista
Lista_numeros = Listbox(mywindow)
Lista_numeros.place(x=350, y=120)

#creacion de boton para guardar la informacion
Btn_ingresa = Button(mywindow, text="Ingresar", command= agregar_info)
Btn_ingresa.place(x=350, y=300)


#-------------------------------------------------------------------
#      Box 3
#-------------------------------------------------------------------
box3=Label(bg="#b48471", width="35", height="21")
box3.place(x=610, y=100)

mywindow.mainloop()
