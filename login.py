import tkinter as tk
from tkinter import messagebox,simpledialog
usuarios_registrados=["sebas","gerson","camba"]
claves_registradas=["1234","abcd","1234"]
tipo_usuario=["administrador","vendedor","comprador"]

def login(usuario,clave):
    for i in range(len(usuarios_registrados)):
        if usuarios_registrados[i] == usuario and claves_registradas[i] == clave:
            messagebox.showinfo("ACCESO","ACCESO CONCEDIDO")
            return tipo_usuario[i]
    return None

def ver_usuarios():
    m_usuarios=""
    for i in range(len(usuarios_registrados)):
        m_usuarios+=(f"USUARIO: {usuarios_registrados[i].upper()}: {tipo_usuario[i].upper()}\n")
    return m_usuarios

def agregar_usuario(usuario,clave,tipo):
    if tipo != "administrador" and tipo != "vendedor" and tipo != "comprador":
        messagebox.showinfo("ERROR DE ACCESO","SOLO SE PUEDE ELEGIR ADMINISTRADOR, VENDEDOR O COMPRADOR")
    elif usuario in usuarios_registrados:
        messagebox.showinfo("ERROR DE USUARIO","ESE USUARIO YA EXISTE")
    else:
        usuarios_registrados.append(usuario)
        claves_registradas.append(clave)
        tipo_usuario.append(tipo)
        messagebox.showinfo("EXITO","CUENTA AGREGADA")

def eliminar_usuario(usuario):
    if usuario in usuarios_registrados:
        i = usuarios_registrados.index(usuario)
        del usuarios_registrados[i]
        del claves_registradas[i]
        del tipo_usuario[i]
        messagebox.showinfo("ELIMINADO",f"EL USUARIO '{usuario.upper()}' FUE ELIMINADO EXITOSAMENTE.")
    else:
        messagebox.showwarning("EL USUARIO NO EXISTE EN EL SISTEMA.")

def modificar_usuario(usuario):
    if usuario in usuarios_registrados:
        i = usuarios_registrados.index(usuario)
        nueva_clave = simpledialog.askstring("NUEVA CLAVE",f"NUEVA CLAVE (ACTUAL: {claves_registradas[i]}):").strip()
        nuevo_tipo = simpledialog.askstring("TIPO",f"NUEVO TIPO (ACTUAL: {tipo_usuario[i].upper()}):").strip().lower()
        if nueva_clave:
            claves_registradas[i] = nueva_clave
        if nuevo_tipo:
            if nuevo_tipo == "administrador" or nuevo_tipo == "vendedor" or nuevo_tipo == "comprador":
                tipo_usuario[i] = nuevo_tipo
            else:
                messagebox.showwarning("TIPO INVALIDO"," SE MANTUVO EL TIPO ANTERIOR")
        messagebox.showinfo("EXITO",f"¡USUARIO '{usuario.upper()}' MODIFICADO EXITOSAMENTE!")
    else:
        messagebox.showwarning("ERROR DE USUARIO","EL USUARIO NO EXISTE EN EL SISTEMA.")
