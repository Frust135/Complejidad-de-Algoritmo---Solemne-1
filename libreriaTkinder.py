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


#creacion de la ventana
mywindow=Tk()
mywindow.geometry("350x400")
mywindow.title("Metodos de búsqueda")

#Comienza ingreso de datos
Ingreso_label = Label(text="Ingrese datos")
Ingreso_label.place(x=22, y=100)

#creo una variable
Ingreso = StringVar()

#creo un espacio donde guardare lo que se ingrese en la variable anterior

User_entry = Entry(textvariable=Ingreso)
User_entry.place(x= 100, y=100)

#creacion lista
Lista_numeros = Listbox(mywindow)
Lista_numeros.place(x=60, y=200)
#creacion de boton para guardar la informacion
Btn_ingresa = Button(mywindow, text="Ingresar", command= agregar_info)
Btn_ingresa.place(x=60, y=150)

mywindow.mainloop()
