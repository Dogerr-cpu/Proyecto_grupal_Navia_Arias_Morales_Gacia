import tkinter as tk
from tkinter import messagebox,simpledialog
import json
import os
datos_usuarios="datos_usuarios_guardados.json"


if os.path.exists(datos_usuarios):
    try:
        with open(datos_usuarios,"r",encoding="utf-8") as f:
            datos_u=json.load(f)
            usuarios_registrados=datos_u.get("usuarios_registrados",["sebas","gerson","camba"])
            claves_registradas=datos_u.get("claves_registradas",["1234","abcd","1234"])
            tipo_usuario=datos_u.get("tipo_usuario",["administrador","vendedor","comprador"])
    except:
        usuarios_registrados=["sebas","gerson","camba"]
        claves_registradas=["1234","abcd","1234"]
        tipo_usuario=["administrador","vendedor","comprador"]
else:
    usuarios_registrados=["sebas","gerson","camba"]
    claves_registradas=["1234","abcd","1234"]
    tipo_usuario=["administrador","vendedor","comprador"]

def guardar_datos_u():
    datos_u={
        "usuarios_registrados":usuarios_registrados,
        "claves_registradas":claves_registradas,
        "tipo_usuario":tipo_usuario
        }
    with open(datos_usuarios,"w",encoding="utf-8") as f:
        json.dump(datos_u,f,ensure_ascii=False,indent=4)

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
    if usuario in usuarios_registrados:
        messagebox.showinfo("ERROR DE USUARIO","ESE USUARIO YA EXISTE")
    elif tipo == 1:
        usuarios_registrados.append(usuario)
        claves_registradas.append(clave)
        tipo_usuario.append("administrador")
        guardar_datos_u()
        messagebox.showinfo("EXITO","CUENTA AGREGADA")
    elif tipo == 2:
        usuarios_registrados.append(usuario)
        claves_registradas.append(clave)
        tipo_usuario.append("vendedor")
        guardar_datos_u()
        messagebox.showinfo("EXITO","CUENTA AGREGADA")
    elif tipo == 3:
        usuarios_registrados.append(usuario)
        claves_registradas.append(clave)
        tipo_usuario.append("comprador")
        guardar_datos_u()
        messagebox.showinfo("EXITO","CUENTA AGREGADA")
    else:
        messagebox.showwarning("ERROR","SOLO SELECIONA EL 1,2 O 3")
def eliminar_usuario(usuario):
    if usuario in usuarios_registrados:
        i = usuarios_registrados.index(usuario)
        del usuarios_registrados[i]
        del claves_registradas[i]
        del tipo_usuario[i]
        guardar_datos_u()
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
        guardar_datos_u()
        messagebox.showinfo("EXITO",f"¡USUARIO '{usuario.upper()}' MODIFICADO EXITOSAMENTE!")
    else:
        messagebox.showwarning("ERROR DE USUARIO","EL USUARIO NO EXISTE EN EL SISTEMA.")
