import tkinter as tk
from tkinter import messagebox,simpledialog
from inventario import ver_productos,vender,registrar_entrada,registrar_salida,ver_movimientos,ver_ventas

def menu_usuario(nombre,ventana):
        ventana_vendedor = tk.Tk()
        ventana_vendedor.title(f"MENU DE VENDEDOR: {nombre.upper()}")
        ventana_vendedor.geometry("1100x600")
        ventana_vendedor.config(bg="Light green")

        frame_izquierda=tk.Frame(ventana_vendedor,bg="green")
        frame_izquierda.pack(padx=20,pady=20,side=tk.LEFT,fill=tk.Y)

        frame_derecha=tk.Frame(ventana_vendedor,bg="green")
        frame_derecha.pack(padx=20,pady=20,side=tk.RIGHT,fill=tk.BOTH,expand=True)
        def opcion1():
            lista_productos=ver_productos()
            cuadro_consola1.delete("1.0",tk.END)

            if lista_productos:
                cuadro_consola1.insert(tk.END,lista_productos)
            else:
                cuadro_consola1.insert(tk.END,"no hay productos ahora")
        def opcion2():
            try:
                cliente = simpledialog.askstring("cliente","INGRESE EL NOMBRE DEL CLIENTE:").strip().lower()
                if cliente is None:return
                if cliente.isalpha():
                    codigo=simpledialog.askstring("codigo","INGRESE EL CODIGO DEL PRODUCTO:").strip()
                    if codigo is None:return
                    codigo=int(codigo)
                    cantidad=simpledialog.askstring("cantidad","INGRESE LA CANTIDAD:").strip()
                    if cantidad is None:return
                    cantidad=int(cantidad)
                    vender(codigo,cantidad,cliente,nombre)
                else:
                      messagebox.showwarning("Error nombre","NO SE DEBE PONER NUMEROS AL NOMBRE")
            except ValueError:
                  messagebox.showerror("Error numeros","INGRESE NUMEROS ENTEROS")

        def opcion3():
            try:
                codigo= simpledialog.askstring("codigo","INGRESE EL CODIGO DEL PRODUCTO QUE VA ENTRAR:").strip()
                if codigo is None:return
                codigo=int(codigo)
                cantidad= simpledialog.askstring("cantidad","INGRESA LA CANTIDAD QUE VA ENTRAR:").strip()
                if cantidad is None:return
                cantidad=int(cantidad)
                registrar_entrada(codigo,cantidad,nombre)
            except ValueError:
                messagebox.showerror("Error numeros","INGRESA NUMEROS ENTEROS")
        def opcion4():
            try:
                codigo= simpledialog.askstring("codigo","INGRESE EL CODIGO DEL PRODUCTO QUE VA SALIR:").strip()
                if codigo is None:return
                codigo=int(codigo)
                cantidad= simpledialog.askstring("cantidad","INGRESA LA CANTIDAD QUE VA SALIR:").strip()
                if cantidad is None:return
                cantidad=int(cantidad)
                registrar_salida(codigo,cantidad,nombre)
            except ValueError:
                messagebox.showerror("Error numeros","INGRESA NUMEROS ENTEROS")
        def opcion5():
            lista_movimientos=ver_movimientos()
            cuadro_consola1.delete("1.0",tk.END)

            if lista_movimientos:
                cuadro_consola1.insert(tk.END,lista_movimientos)
            else:
                cuadro_consola1.insert(tk.END,"NO HAY TODAVIA MOVIMIENTOS")
        def opcion6():
            lista_ventas=ver_ventas()
            cuadro_consola1.delete("1.0",tk.END)
            if lista_ventas:
                cuadro_consola1.insert(tk.END,lista_ventas)
            else:
                cuadro_consola1.insert(tk.END,"NO HAY VENTAS TODAVIA")
        def opcion7():
            ventana_vendedor.destroy()
            ventana.deiconify()
        
        tk.Label(frame_izquierda,text="MENU",fg="black",bg="green",font=("Arial",14,"bold")).pack(pady=10)
        tk.Button(frame_izquierda,text="1. Ver productos",bg="green",fg="white",width=20,command=opcion1).pack(pady=5)
        tk.Button(frame_izquierda,text="2. Vender",bg="green",fg="white",width=20,command=opcion2).pack(pady=5)
        tk.Button(frame_izquierda,text="3. Registrar entrada",bg="green",fg="white",width=20,command=opcion3).pack(pady=5)
        tk.Button(frame_izquierda,text="4. Registrar salida",bg="green",fg="white",width=20,command=opcion4).pack(pady=5)
        tk.Button(frame_izquierda,text="5. Ver entradas y salidas",bg="green",fg="white",width=20,command=opcion5).pack(pady=5)
        tk.Button(frame_izquierda,text="6. Ver ventas",bg="green",fg="white",width=20,command=opcion6).pack(pady=5)
        tk.Button(frame_izquierda,text="7. Volver al login",bg="red",fg="white",width=20,command=opcion7).pack(pady=5)
        cuadro_consola1 = tk.Text(frame_derecha, width=40, height=18, font=("Courier", 10), bg="blue",fg="white", bd=2)
        cuadro_consola1.pack(fill=tk.BOTH,expand=True)
        cuadro_consola1.insert(tk.END, "SELECCIONA CUALQUIERA DE LAS OPCIONES.....")
        ventana_vendedor.mainloop()
