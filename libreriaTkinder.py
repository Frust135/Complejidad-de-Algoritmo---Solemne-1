from tkinter import *
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
    if s==2:
        User_entry2 = Entry(textvariable=Ingreso)
        User_entry2.place(x= 40, y=180)

        User_entry3 = Entry(textvariable=Ingreso)
        User_entry3.place(x= 40, y=200)

        User_entry4 = Entry(textvariable=Ingreso)
        User_entry4.place(x= 40, y=220)
    if s==1:
        User_entry1 = Entry(textvariable=Ingreso)
        User_entry1.place(x= 40, y=180)


#creacion de la ventana
mywindow=Tk()
mywindow.geometry("893x416")
mywindow.title("Metodos de búsqueda")
mywindow['bg'] = '#72382e'

Titulo=Label(text="Métodos de ordenamiento" ,font=("Cambria",15),fg="#210e0c" , bg="#e4ba9f", width="893", height="3")

Titulo.pack()

#-------------------------------------------------------------------
#      Ingreso de datos
#-------------------------------------------------------------------
box1=Label(bg="#b48471", width="35", height="19")
box1.place(x=25, y=100)

Ingreso_label = Label(text="Ingrese la opción", bg="#b48471", font=("Cambria",13), fg="#210e0c")
Ingreso_label.place(x=29, y=100)

Seleccion = IntVar()

rdioNumeros = Radiobutton(mywindow, text="Ingresar números",bg="#b48471",fg="#210e0c",font=("Cambria",10),variable=Seleccion, value=1, command=Creacion_entrada)
rdioNumeros.place(x=25, y=130)

rdioRandom = Radiobutton(mywindow, text="Ingresar números random",bg="#b48471",fg="#210e0c",font=("Cambria",10),variable=Seleccion, value=2, command=Creacion_entrada)
rdioRandom.place(x=25, y=150)


#creo una variable
Ingreso = StringVar()

#creo un espacio donde guardare lo que se ingrese en la variable anterior

User_entry = Entry(textvariable=Ingreso)
User_entry.place(x= 110, y=260)

#creacion lista
Lista_numeros = Listbox(mywindow)
Lista_numeros.place(x=60, y=250)
#creacion de boton para guardar la informacion
Btn_ingresa = Button(mywindow, text="Ingresar", command= agregar_info)
Btn_ingresa.place(x=60, y=300)

#Se muestra lista ordenada y tabla
box2=Label(bg="#b48471", width="35", height="19")
box2.place(x=320, y=100)

#Se muestra el grafico
box3=Label(bg="#b48471", width="35", height="19")
box3.place(x=610, y=100)

mywindow.mainloop()
