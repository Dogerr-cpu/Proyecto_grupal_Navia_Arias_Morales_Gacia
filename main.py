import tkinter as tk
from tkinter import messagebox,simpledialog
from login import login
from admin import menu_administrador
from usuario import menu_usuario

def main():
    ventana = tk.Tk()
    ventana.title(f"TIENDA DE COMPUTADORAS ")
    ventana.geometry("1100x600")
    ventana.config(bg="Light green")
    def opcion1():
        ventana.withdraw()
        ventana1 = tk.Tk()
        ventana1.title(f"TIENDA DE COMPUTADORAS ")
        ventana1.geometry("1100x600")
        ventana1.config(bg="Light green")
        tk.Label(ventana1,text="BIENVENIDO A LA TIENDA DE COMPUTADORAS",bg="Light green",fg="black",font=("Arial",30,"bold")).pack(pady=90)
        tk.Label(ventana1,text="usuario",fg="black",font=("Arial",12),bg="Light green").pack(pady=5)
        usuario_ingresado=tk.Entry(ventana1,font=("arial",12),width=20)
        usuario_ingresado.pack(pady=5)
        tk.Label(ventana1,text="contraseña",fg="black",font=("Arial",12),bg="Light green").pack(pady=10)
        clave_ingresada=tk.Entry(ventana1,font=("arial",12),width=20, show="*")
        clave_ingresada.pack(pady=5)
        tk.Button(ventana1,text="INICIAR SESION",bg="red",fg="white",width=20,command=lambda:inicia(usuario_ingresado,clave_ingresada,ventana1,ventana)).pack(pady=5)
    
    def inicia(usuario_ingresado,clave_ingresada,ventana,ventana_global):
        usuario1=usuario_ingresado.get().strip().lower()
        clave1=clave_ingresada.get().strip().lower()
        tipo=login(usuario1,clave1)

        if tipo == "administrador":
            messagebox.showinfo("LOGIN",f"===BIENVENIDO AL MENU DE {tipo.upper()}===")
            ventana.destroy()
            menu_administrador(usuario1,ventana_global)
            
        elif tipo == "vendedor":
            messagebox.showinfo("LOGIN",f"===BIENVENIDO AL MENU DE {tipo.upper()}===")
            ventana.destroy()
            menu_usuario(usuario1,ventana_global)
    
        else:
            messagebox.showwarning("ERROR","USUARIO O CONTRASEÑA INVALIDO")
    
    tk.Label(ventana,text="BIENVENIDO A LA TIENDA DE COMPUTADORAS",fg="black",font=("Arial",30,"bold")).pack(pady=90)
    tk.Button(ventana,text="1. INICIAR SESION",bg="black",fg="white",width=20,command=opcion1).pack(pady=15)
    tk.Button(ventana,text="2. SALIR DEL SISTEMA",bg="black",fg="white",width=20,command=ventana.destroy).pack(pady=15)

    ventana.mainloop()
main()
