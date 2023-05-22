import tkinter
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox

#-------------------Ventana Inicio------------
ventana=tkinter.Tk()
ventana.title("Calculadora De Probabilidad")
ventana.geometry("500x200")
ventana.resizable(0,0)
ventana.iconbitmap("icono.ico")
#-------------------Fin Ventana---------------
#-------------------Contenido de la ventana-------------------------------
#-------------------Titulo--------------------
titulo = tkinter.Label(ventana, text = "Bienvenido. Porfavor escoge el tipo de Probabilidad", font="arial")
titulo.pack()
#---------------------Acciones Botones--------
def b1(): 
    uniforme=tkinter.Toplevel()
    uniforme.geometry("500x500")
    uniforme.title("Probabilidad Uniforme")
    uniforme.resizable(0,0)
    uniforme.iconbitmap("icono.ico")
    formula = tkinter.Label(uniforme, text = "Formula: ", font="arial")
    formula.pack()
    formula.place(x=10, y=40)
    imagen = ImageTk.PhotoImage(Image.open("imgUniforme.png"))
    imgLabel = Label(uniforme, image = imagen).place(x=100, y=20)
    def calcular_promedio():
            n1 = Txtbox.get()
            n2 = Txtbox1.get()
            if not n1:
                messagebox.showerror("Error","El campo no puede estar vacio")
            else:
                prom = float(n1 + n2)/2
                2
                messagebox.showinfo("Resultado",
                                    f"El primedio es: {prom:.2f}")
    lbltxt = Label(uniforme, text = "Digita el primer valor: ", font="arial")
    lbltxt.place(x=10, y=100)
    Txtbox = Entry(uniforme,)
    Txtbox.place(x=210, y=106)
    lbltxt1 = Label(uniforme, text = "Digita el segundo valor: ", font="arial")
    lbltxt1.place(x=10, y=150)
    Txtbox1 = Entry(uniforme)
    Txtbox1.place(x=225, y=156)
    lbltxt2 = Label(uniforme, text = "Digita el valor de la condición: ", font="arial")
    lbltxt2.place(x=10, y=200)
    Txtbox2 = Entry(uniforme)
    Txtbox2.place(x=280, y=206)
        
    btn_calcular = tk.Button(uniforme, text = "Promedio", command=calcular_promedio, fg="white", bg="black", font="arial", cursor="hand2")
    btn_calcular.place(x=380, y=150,)

            
    uniforme.mainloop()

    
def b2():
    exponencial=tkinter.Toplevel()
    exponencial.geometry("500x500")
    exponencial.title("Probabilidad Exponencial")
    exponencial.resizable(0,0)
    exponencial.iconbitmap("icono.ico")
    formula2 = tkinter.Label(exponencial, text = "Formula: ", font="arial")
    formula2.pack()
    formula2.place(x=10, y=40)
    imagen2 = ImageTk.PhotoImage(Image.open("imgExponen.png"))
    imgLabel2 = Label(exponencial, image = imagen2).place(x=100, y=20)
    exponencial.mainloop()
    
def b3():
    normal=tkinter.Toplevel()
    normal.geometry("500x500")
    normal.title("Probabilidad Normal")
    normal.resizable(0,0)
    normal.iconbitmap("icono.ico")
    formula3 = tkinter.Label(normal, text = "Formula: ", font="arial")
    formula3.pack()
    formula3.place(x=10, y=40)
    imagen3 = ImageTk.PhotoImage(Image.open("imgNormal.png"))
    imgLabel3 = Label(normal, image = imagen3).place(x=100, y=20)
    normal.mainloop()
#---------------------Botones-----------------
boton1 = tkinter.Button(ventana,text="Uniforme",command=b1, fg="white", bg="black", font="arial", cursor="hand2")
boton1.pack()
boton1.place(x=10, y=80, height= 60, width =120)

boton2 = tkinter.Button(ventana,text="Exponencial",command=b2, fg="white", bg="black", font="arial", cursor="hand2")
boton2.pack()
boton2.place(x=190, y=80, height= 60, width =120)

boton3 = tkinter.Button(ventana,text="Normal",command=b3, fg="white", bg="black", font="arial", cursor="hand2")
boton3.pack()
boton3.place(x=370, y=80, height= 60, width =120)

ventana.mainloop()

