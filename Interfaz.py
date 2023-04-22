#Importacion de librerias 
import tkinter as tk  #tkinter framework para interfaz python
from tkinter import *
from tkinter.filedialog import askopenfilename #framework para abrir el navegador
import os
import principal
#import principal

rutaPed = "null" 
rutaGuia = "null"
rutaFact = "null"
cont = 0

class Interfaz():
    

    def __init__(self):
        self.root = tk.Tk()
        self.pagina_inicio()
        self.root.mainloop()


    def update1(self):
        Tk().withdraw() 
        filename = askopenfilename() 
        global rutaPed
        rutaPed = filename
        name1 = os.path.basename(rutaPed)
        self.contenedor1.config(text=name1)
        print(name1)

    def update2(self):
        Tk().withdraw() 
        filename = askopenfilename() 
        global rutaGuia
        rutaGuia = filename
        name2 = os.path.basename(rutaGuia)
        self.contenedor2.config(text=name2)
        print(name2)

    def update3(self):
        Tk().withdraw() 
        filename = askopenfilename() 
        global rutaFact
        rutaFact = filename
        name3 = os.path.basename(rutaFact)
        self.contenedor3.config(text=name3)
        print(name3)

    def update4(self):

        resultados = principal.revisarDocs(rutaFact, rutaPed, rutaGuia)
        
        self.dato1.config(text="Tipo cambio: " + str(resultados["TIPO CAMBIO"]))
        self.dato2.config(text="Peso bruto: " + str (resultados["PESO BRUTO"]))
        self.dato3.config(text="DTA: " + str(resultados["DTA"]))
        self.dato4.config(text="IVA: " + str(resultados["IVA"]))
        self.dato5.config(text="F.P. IVA: " + str(resultados["F.P. IVA"]))
        self.dato6.config(text="NUM GUIA: " + str (resultados["NUM GUIA"]))
        self.dato7.config(text="NUM FACTURA: " + str (resultados["NUM FACTURA"]))
        

    def pagina_inicio(self):

        
        self.root.geometry("300x400")
        self.root.resizable(width=False, height=False)

        self.BgLabel = tk.Label(self.root)
        self.BgLabel.config(bg="#030030",width=300,height=8)
        self.BgLabel.place(x= 0, y=0)

        self.TitleMarca = tk.Label(self.root,text="Doc Recon")
        self.TitleMarca.config(font=("LEMON MILK",8))
        self.TitleMarca.place(x=115,y=380)

        self.T1 = tk.Label(self.root,text="Bienvenido")
        self.T1.config(fg = "white",bg='#03002d',font=("LEMON MILK", 16))
        self.T1.place(x=85,y=30)

        self.Txt1 = tk.Label(self.root,text="Para continuar, sube el archivo \n para comenzar el analisis")
        self.Txt1.config(fg = "white",bg='#03002d',font=("Inter", 8))
        self.Txt1.place(x=70,y=70)

        self.Txt2 = tk.Label(self.root,text="Presiona el botón para subir tu archivo")
        self.Txt2.config(fg="#565656",bg="#f0f0f0",font=("Inter",10))
        self.Txt2.place(x=30,y=150)

        #boton donde activa por un comando la funcion de cargar archivos y este solo funciona al ser precionado
        self.Bsubir1 = tk.Button(self.root,text="Subir", command=self.update1)
        self.Bsubir1.config(fg="white", bg= "#3d3d3d",font=("Inter",10),width=10,height=2)
        self.Bsubir1.place(x=190,y=180)
        
        self.Bsubir2 = tk.Button(self.root,text="Subir", command=self.update2)
        self.Bsubir2.config(fg="white", bg= "#3d3d3d",font=("Inter",10),width=10,height=2)
        self.Bsubir2.place(x=190,y=240)

        self.Bsubir3 = tk.Button(self.root,text="Subir", command=self.update3)
        self.Bsubir3.config(fg="white", bg= "#3d3d3d",font=("Inter",10),width=10,height=2)
        self.Bsubir3.place(x=190,y=300)

        self.Bsubir4 = tk.Button(self.root,text="Siguiente", command=self.pagina_segunda)
        self.Bsubir4.config(fg="white", bg= "#3d3d3d",font=("Inter",10),width=10,height=1)
        self.Bsubir4.place(x=190,y=350)

        self.contenedor1 = tk.Label(self.root,text="Pedimento")
        self.contenedor1.config(bg="#B8B8B8",font=("Inter",10),width=20,height=2)
        self.contenedor1.place(x=20,y=180)

        self.contenedor2 = tk.Label(self.root,text="Guia de embarque")
        self.contenedor2.config(bg="#B8B8B8",font=("Inter",10),width=20,height=2)
        self.contenedor2.place(x=20,y=240)

        self.contenedor3 = tk.Label(self.root,text="Factura")
        self.contenedor3.config(bg="#B8B8B8",font=("Inter",10),width=20,height=2)
        self.contenedor3.place(x=20,y=300)

    def pagina_segunda(self):

        self.root1 = tk.Tk()
        self.root1.geometry("500x300")
        self.root1.resizable(width=False, height=False)
        self.root.destroy()
        
        self.barralateral = tk.Label(self.root1)
        self.barralateral.config(bg="#ECECEC",width=25,height=30)
        self.barralateral.place(x=0,y=0)

        self.contenido = tk.Label(self.root1, text="")
        self.contenido.config(bg="#03002d",fg="white",font=("Inter",10),width=50,height=30)
        self.contenido.place(x=180,y=0)

        self.text2 = tk.Label(self.root1,text="Verifica los resultados del análisis")
        self.text2.config(bg="#ECECEC", font=("Inter",7),width=25,height=2)
        self.text2.place(x=10,y=150)

        self.text3 = tk.Label(self.root1,text=" Análisis \n Completo")
        self.text3.config(bg="#ECECEC", font=("LEMON MILK",14),width=10,height=2)
        self.text3.place(x=20,y=200)

        self.dato1 = tk.Label(self.root1, text="hola")
        self.dato1.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato1.place(x=200,y=0)

        
        self.dato2 = tk.Label(self.root1, text="hola")
        self.dato2.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato2.place(x=200,y=30)

        
        self.dato3 = tk.Label(self.root1, text="hola")
        self.dato3.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato3.place(x=200,y=60)

        
        self.dato4 = tk.Label(self.root1, text="hola")
        self.dato4.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato4.place(x=200,y=90)

        
        self.dato5 = tk.Label(self.root1, text="hola")
        self.dato5.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato5.place(x=200,y=120)

        
        self.dato6 = tk.Label(self.root1, text="hola")
        self.dato6.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato6.place(x=200,y=150)


        self.dato7 = tk.Label(self.root1, text="hola")
        self.dato7.config(bg="#03002d",fg="white",font=("Inter",10))
        self.dato7.place(x=200,y=180)

        self.update4()
        
         
Interfaz()
    


