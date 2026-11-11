import tkinter as tk
from tkinter import messagebox, simpledialog
from inventario import ver_productos, agregar_producto, registrar_entrada, registrar_salida, ver_movimientos, ver_ventas,vender,reeembolso
from login import ver_usuarios, agregar_usuario, eliminar_usuario, modificar_usuario

def menu_administrador(nombre,ventana):
    ventana_administrador = tk.Tk()
    ventana_administrador.title(f"MENU DE ADMINISTRADOR: {nombre.upper()}")
    ventana_administrador.geometry("1100x600")
    ventana_administrador.config(bg="Light green")
    ventana_administrador.iconbitmap("Mejorado_creo.ico")

    def mostrar_productos_en_pantalla():
        lista_de_productos = ver_productos() 
        cuadro_consola.delete("1.0", tk.END)
    
        if lista_de_productos:
            cuadro_consola.insert(tk.END, lista_de_productos)
        else:
            cuadro_consola.insert(tk.END, "No hay productos registrados o la función no retornó texto.")

    def opcion_2():
        try:
            codigo = simpledialog.askstring("Producto", "INGRESE EL CODIGO:")
            if codigo is None: return 
            codigo = int(codigo)
            nombre_producto = simpledialog.askstring("Producto", "INGRESE EL NOMBRE DEL PRODUCTO:").strip().lower()
            if nombre_producto is None: return
            if nombre_producto.replace(" ", "").isalpha():
                precio = simpledialog.askstring("Producto", "INGRESE EL PRECIO DEL PRODUCTO ($):").strip()
                if precio is None: return
                precio=int(precio)
                stock = simpledialog.askstring("Producto", "INGRESE EL STOCK:").strip()
                if stock is None: return
                stock=int(stock)
                agregar_producto(codigo, nombre_producto, precio, stock)
                mostrar_productos_en_pantalla()
            else:
                messagebox.showwarning("Error de nombre", "NO PUEDES PONER NUMEROS EN NOMBRE DEL PRODUCTO")
        except ValueError:
            messagebox.showerror("Error de datos", "=== INGRESE NUMEROS ENTEROS ===")

    def opcion3():
        try:
            codigo=simpledialog.askstring("Codigo","INGRESE EL CODIGO:").strip()
            if codigo is None:return
            codigo=int(codigo)
            cantidad=simpledialog.askstring("Cantidad","INGRESA LA CANTIDAD QUE ENTRA:").strip()
            if cantidad is None:return
            cantidad=int(cantidad)
            registrar_entrada(codigo,cantidad,nombre)
        except ValueError:
            messagebox.showerror("Error de datos", "=== INGRESE NUMEROS ENTEROS ===")

    def opcion4():
        try:
            codigo=simpledialog.askstring("Codigo","INGRESE EL CODIGO:").strip()
            if codigo is None:return
            codigo=int(codigo)
            cantidad=simpledialog.askstring("Cantidad","INGRESA LA CANTIDAD QUE SALE:").strip()
            if cantidad is None:return
            cantidad=int(cantidad)
            registrar_salida(codigo,cantidad,nombre)
        except ValueError:
            messagebox.showerror("Error de datos","=== INGRESE NUMEROS ENTEROS ===")
    def mostrar_entradas_y_salidas():
        lista_entradas_salidas=ver_movimientos()
        cuadro_consola.delete("1.0",tk.END)

        if lista_entradas_salidas:
            cuadro_consola.insert(tk.END,lista_entradas_salidas)
        else:
            cuadro_consola.insert(tk.END,"NO HAY ENTRADAS Y SALIDAS AHORA")
    def mostrar_ventas():
        lista_ventas=ver_ventas()
        cuadro_consola.delete("1.0",tk.END)

        if lista_ventas:
            cuadro_consola.insert(tk.END,lista_ventas)
        else:
            cuadro_consola.insert(tk.END,"NO HAY VENTAS AHORA")
    def mostrar_usuarios():
        lista_usuarios=ver_usuarios()
        cuadro_consola.delete("1.0",tk.END)

        if lista_usuarios:
            cuadro_consola.insert(tk.END,lista_usuarios)
        else:
            cuadro_consola.insert(tk.END,"NO HAY USUARIOS AHORA")
    def opcion8():
        try:
            usuario_nuevo=simpledialog.askstring("usuario","INGRESA UN USUARIO:").lower().strip()
            if not usuario_nuevo: return
            clave_nueva=simpledialog.askstring("clave",f"INGRESA SU NUEVA CLAVE DE {usuario_nuevo.upper()}:").strip().lower()
            tipo_nuevo=simpledialog.askstring("accesos",f"""QUE ACCESOS QUIERE PARA EL USUARIO {usuario_nuevo.upper()} SELECCIONA CON UN NUMERO:
            1.Administrador
            2.vendedor""")
            tipo_nuevo=int(tipo_nuevo)
            agregar_usuario(usuario_nuevo,clave_nueva,tipo_nuevo)
        except ValueError:
            messagebox.showwarning("Error","SOLO DEBES PONER NUMERO ENTERO EN ACCESO")
    def opcion9():
        usuario_eliminar=simpledialog.askstring("Usuario eliminar","INGRESA EL USUARIO A ELIMINAR: ").strip().lower()
        eliminar_usuario(usuario_eliminar)
    def opcion10():
        usuario_modificar=simpledialog.askstring("Modificar","INGRESA EL USUARIO QUE DESEA CAMBIAR SU CONTRASEÑA:").strip().lower()
        modificar_usuario(usuario_modificar)
    def vender_admin():
        try:
            mostrar_productos_en_pantalla()
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
                mostrar_productos_en_pantalla()
            else:
                messagebox.showwarning("Error nombre","NO SE DEBE PONER NUMEROS AL NOMBRE")
        except ValueError:
                  messagebox.showerror("Error numeros","INGRESE NUMEROS ENTEROS")
    def opcion_reembolso():
        try:
            mostrar_ventas()
            cliente= simpledialog.askstring("NOMBRE DEL USUARIO","INGRESE EL NOMBRE DEL CLIENTE PARA REEMBOLSAR").strip().lower()
            if cliente is None:return
            cantidad= simpledialog.askstring("cantidad","INGRESA LA CANTIDAD:").strip()
            if cantidad is None:return
            cantidad=int(cantidad)
            reeembolso(cliente,cantidad,nombre)
            mostrar_productos_en_pantalla()
        except ValueError:
            messagebox.showerror("Error numeros","INGRESA NUMEROS ENTEROS")
    def opcion11():
        ventana_administrador.destroy()
        ventana.deiconify()
    
    frame_izquierda = tk.Frame(ventana_administrador, bg="green")
    frame_izquierda.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

    frame_derecha = tk.Frame(ventana_administrador, bg="white")
    frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    tk.Label(frame_izquierda, text="MENU", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
    menu_usuarios = tk.Frame(frame_izquierda, bg="green")
    menu_productos = tk.Frame(frame_izquierda, bg="green")
    menu_ventas = tk.Frame(frame_izquierda, bg="green")

    def desplegar(menu):
        if menu.winfo_ismapped():
            menu.pack_forget()
        else:
            menu_usuarios.pack_forget()
            menu_productos.pack_forget()
            menu_ventas.pack_forget()
            menu.pack(fill=tk.X,pady=15)
            
    tk.Button(frame_izquierda, text="GESTIONAR USUARIOS", width=20,bg="green",fg="white",command=lambda: desplegar(menu_usuarios)).pack(pady=5)
    tk.Button(menu_usuarios, text="Ver usuarios", command=mostrar_usuarios).pack(fill=tk.X)
    tk.Button(menu_usuarios, text="Agregar usuario", command=opcion8).pack(fill=tk.X)
    tk.Button(menu_usuarios, text="Eliminar usuario", command=opcion9).pack(fill=tk.X)
    tk.Button(menu_usuarios, text="Modificar usuario", command=opcion10).pack(fill=tk.X)

    tk.Button(frame_izquierda, text="GESTIONAR PRODUCTOS", width=20,bg="green",fg="white",command=lambda: desplegar(menu_productos)).pack(pady=5)
    tk.Button(menu_productos, text="Ver productos", command=mostrar_productos_en_pantalla).pack(fill=tk.X)
    tk.Button(menu_productos, text="Agregar producto", command=opcion_2).pack(fill=tk.X)
    tk.Button(menu_productos, text="Registrar entrada", command=opcion3).pack(fill=tk.X)
    tk.Button(menu_productos, text="Registrar salida", command=opcion4).pack(fill=tk.X)
    tk.Button(menu_productos, text="Ver entradas y salidas", command=mostrar_entradas_y_salidas).pack(fill=tk.X)

    tk.Button(frame_izquierda, text="VENTAS", width=20,bg="green",fg="white",command=lambda: desplegar(menu_ventas)).pack(pady=10)
    tk.Button(menu_ventas, text="Ver ventas", command=mostrar_ventas).pack(fill=tk.X)
    tk.Button(menu_ventas, text="Ventas", command=vender_admin).pack(fill=tk.X)
    tk.Button(menu_ventas,text="Hacer el reembolso",command=opcion_reembolso).pack(fill=tk.X)

    tk.Button(frame_izquierda, text="VOLVER AL LOGIN", bg="red", fg="white",width=20, command=opcion11).pack(pady=15)
    tk.Label(frame_derecha, text="VISUALIZACION", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    cuadro_consola = tk.Text(frame_derecha, width=40, height=18, font=("Courier", 10), bg="blue",fg="white", bd=2)
    cuadro_consola.pack(fill=tk.BOTH, expand=True)
    cuadro_consola.insert(tk.END, "SELECCIONA CUALQUIERA DE LAS OPCIONES.....")
    ventana_administrador.mainloop()
