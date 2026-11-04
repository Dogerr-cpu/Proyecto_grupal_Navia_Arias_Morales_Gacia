import tkinter as tk
from tkinter import messagebox,simpledialog
codigos=[1,2,3]
nombres_productos=["laptop","mouse","teclado"]
precios=[12000,250,600]
stocks=[5,20,10]

movimientos=[]
ventas=[]
clientes_ventas=[]

def ver_productos():
    productos_disponibles=""
    for i in range(len(codigos)):
        productos_disponibles+=(f"CODIGO {codigos[i]}: {nombres_productos[i]:<10} | PRECIO DOLARES: {precios[i]:<10}$ | PRECIO BS: {precios[i]*12:<10.2f} BS | STOCK: {stocks[i]}\n")
    return productos_disponibles
    
def buscar_producto(codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1

def agregar_producto(codigo,nombre,precio,stock):
    if buscar_producto(codigo) != -1:
        messagebox.showinfo("ERROR EN CODIGO","EL CODIGO YA EXISTE") 
    elif precio <= 0 or stock < 0:
        messagebox.showinfo("DATOS INVALIDOS","INGRESA DATOS VALIDOS")
    else:
        codigos.append(codigo)
        nombres_productos.append(nombre)
        precios.append(precio)
        stocks.append(stock)
        messagebox.showinfo("EXITO", "PRODUCTO AGREGADO CORRECTAMENTE")
        

def registrar_entrada(codigo,cantidad,responsable):
    posicion=buscar_producto(codigo)
    if posicion == -1:
        messagebox.showinfo("ERROR ENCONTRAR","PRODUCTO NO ENCONTRADO")
    elif cantidad <= 0:
        messagebox.showinfo("DATOS INVALIDOS","INGRESA DATOS VALIDOS")
    else:
        stocks[posicion]=stocks[posicion]+cantidad
        movimientos.append(f"ENTRADA - {nombres_productos[posicion]:<8} | CANTIDAD: {cantidad:<5} | POR: {responsable}\n")
        messagebox.showinfo("EXITO","ENTRADA REGISTRADA")

def registrar_salida(codigo,cantidad,responsable):
    posicion=buscar_producto(codigo)
    if posicion == -1:
        messagebox.showinfo("ERROR ENCONTRAR","PRODUCTO NO ENCONTRADO")
    elif cantidad <= 0:
        messagebox.showinfo("DATOS INVALIDOS","INGRESA DATOS VALIDOS")
    elif cantidad > stocks[posicion]:
        messagebox.showinfo("ERROR STOCK","NO HAY STOCK SUFICIENTE")
    else:
        stocks[posicion]=stocks[posicion]-cantidad
        movimientos.append(f"SALIDA - {nombres_productos[posicion]:<8} | CANTIDAD: {cantidad:<5} | POR: {responsable}\n")
        messagebox.showinfo("EXITO","SALIDA REGISTRADA")

def vender(codigo,cantidad,cliente,vendedor):
    posicion=buscar_producto(codigo)
    if posicion == -1:
        messagebox.showinfo("ERROR DE ENCONTRAR PRODUCTO","PRODUCTO NO ENCONTRADO")
    elif cantidad <= 0:
        messagebox.showinfo("ERROR DE CANTIDAD","INGRESE UNA CANTIDAD VALIDA")
    elif cantidad > stocks[posicion]:
        messagebox.showinfo("ERROR DE STOCK","FALTA DE STOCK")
    else:
        total=precios[posicion]*cantidad
        stocks[posicion]=stocks[posicion]-cantidad
        ventas.append(f"{nombres_productos[posicion]} x {cantidad} = ${total} - CLIENTE: {cliente}\n")
        clientes_ventas.append(cliente)
        movimientos.append(f"SALIDA (VENTA) - {nombres_productos[posicion]} - CANTIDAD: {cantidad} - POR: {vendedor}\n")
        messagebox.showinfo("EXITO",f"VENTA REALIZADA. TOTAL: ${total}")

def ver_movimientos():
    print("="*50)
    print("ENTRADAS Y SALIDAS")
    print("="*50)
    movimiento_n_y_s=""
    for movimiento in movimientos:
        movimiento_n_y_s+=movimiento
    return movimiento_n_y_s
def ver_ventas():
    print("="*50)
    print("VENTAS REALIZADAS")
    print("="*50)
    ventas_ver=""
    for venta in ventas:
        ventas_ver+=venta
    return ventas_ver

def ver_mis_compras(cliente):
    print("="*50)
    print("MIS COMPRAS")
    print("="*50)
    c_ventas=""
    for i in range(len(ventas)):
        if clientes_ventas[i] == cliente:
            c_ventas+=ventas[i]
    return c_ventas
