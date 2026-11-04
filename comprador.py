import tkinter as tk
from tkinter import messagebox,simpledialog
from inventario import ver_productos,vender,ver_mis_compras

def menu_comprador(nombre,ventana):
    ventana_comprador=tk.Tk()
    ventana_comprador.title(F"MENU DE COMPRADOR: {nombre}")
    ventana_comprador.geometry("1100x600")
    ventana_comprador.config(bg="Light green")
    frame_izquierdo=tk.Frame(ventana_comprador,bg="green")
    frame_izquierdo.pack(padx=20,pady=20,side=tk.LEFT,fill=tk.Y)

    frame_derecho=tk.Frame(ventana_comprador,bg="green")
    frame_derecho.pack(padx=20,pady=20,side=tk.RIGHT,fill=tk.BOTH,expand=True)
    def opcion1():
        lista_productos=ver_productos()
        cuadro_ventana.delete("1.0",tk.END)

        if lista_productos:
            cuadro_ventana.insert(tk.END,lista_productos)
        else:
            cuadro_ventana.insert(tk.END,"NO HAY PRODUCTOS TODAVIA")
    def opcion2():
        try:
            codigo= simpledialog.askstring("codigo","INGRESE EL CODIGO DEL PRODUCTO QUE DESEA COMPRAR:").strip()
            if codigo is None:return
            codigo=int(codigo)
            cantidad= simpledialog.askstring("cantidad","INGRESA LA CANTIDAD:").strip()
            if cantidad is None:return
            cantidad=int(cantidad)
            vender(codigo,cantidad,nombre,nombre)
        except ValueError:
            messagebox.showerror("Error numeros","INGRESA NUMEROS ENTEROS")
    def opcion3():
        ver_compras=ver_mis_compras(nombre)
        cuadro_ventana.delete("1.0",tk.END)
        if ver_compras:
            cuadro_ventana.insert(tk.END,ver_compras)
        else:
            cuadro_ventana.insert(tk.END,"NO TENGO COMPRAS TODAVIA")
    def opcion4():
        ventana_comprador.destroy()
        ventana.deiconify()
    tk.Label(frame_izquierdo,text="MENU",font=("Arial",14,"bold"),fg="black",bg="green").pack(pady=10)
    tk.Button(frame_izquierdo,text="1. Ver productos",width=20,bg="green",fg="white",command=opcion1).pack(pady=5)
    tk.Button(frame_izquierdo,text="2. Comprar",width=20,bg="green",fg="white",command=opcion2).pack(pady=5)
    tk.Button(frame_izquierdo,text="3. Ver mis compras",width=20,bg="green",fg="white",command=opcion3).pack(pady=5)
    tk.Button(frame_izquierdo,text="4. Volver al login",width=20,bg="red",fg="white",command=opcion4).pack(pady=5)
    cuadro_ventana=tk.Text(frame_derecho,width=40,height=18,font=("Courier",10),bg="blue",fg="white",bd=2)
    cuadro_ventana.pack(expand=True,fill=tk.BOTH)
    cuadro_ventana.insert(tk.END,"SELECCIONA CUALQUIERA DE LAS OPCIONES.....")
    ventana_comprador.mainloop()
