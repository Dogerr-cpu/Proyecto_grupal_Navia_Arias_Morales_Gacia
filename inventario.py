import tkinter as tk
from tkinter import messagebox,simpledialog,filedialog
import json
import os

Archivo_tienda="datos_tienda.json"

if os.path.exists(Archivo_tienda):
    try:
        with open(Archivo_tienda,"r",encoding="utf-8") as a:
            datos=json.load(a)
            codigos=datos.get("codigos",[1,2,3])
            nombres_productos=datos.get("nombres_productos",["laptop","mouse","teclado"])
            precios=datos.get("precios",[12000,250,600])
            stocks=datos.get("stocks",[5,20,10])
            movimientos=datos.get("movimientos",[])
            ventas=datos.get("ventas",[])
            clientes_ventas=datos.get("clientes_ventas",[])
            rutas_imagenes = datos.get("rutas_imagenes", ["", "", ""])
    except:
        codigos=[1,2,3]
        nombres_productos=["laptop","mouse","teclado"]
        precios=[12000,250,600]
        stocks=[5,20,10]
        movimientos=[]
        ventas=[]
        clientes_ventas=[]
        rutas_imagenes =["", "", ""]
else:
    codigos=[1,2,3]
    nombres_productos=["laptop","mouse","teclado"]
    precios=[12000,250,600]
    stocks=[5,20,10]
    movimientos=[]
    ventas=[]
    clientes_ventas=[]
    rutas_imagenes = ["", "", ""]
def guardar_datos():
    datos={
        "codigos":codigos,
        "nombres_productos":nombres_productos,
        "precios":precios,
        "stocks":stocks,
        "movimientos":movimientos,
        "ventas":ventas,
        "clientes_ventas":clientes_ventas,
        "rutas_imagenes": rutas_imagenes
    }
    with open(Archivo_tienda,"w",encoding="utf-8") as a:
        json.dump(datos,a,indent=4,ensure_ascii=False)

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
        guardar_datos()
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
        guardar_datos()
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
        guardar_datos()
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
        guardar_datos()
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

def reeembolso(cliente,cantidad,nombre):
    if cantidad <= 0:
        messagebox.showinfo("ERROR CANTIDAD","INGRESA UNA CANTIDAD VALIDA")
        return
    verificar = -1
    producto_encontrado=""
    venta_texto=""
    for i in range(len(clientes_ventas)):    
        if cliente == clientes_ventas[i]:
            verificar=i
            venta_texto=ventas[i]
            producto_encontrado=venta_texto.split("x")[0].strip().lower()
            break    
    if verificar == -1 :
        messagebox.showinfo("ERROR USUARIO","NO ENCUENTRO EL USUARIO")
        return
    posicion_producto=-1
    for p in range(len(nombres_productos)):
        if nombres_productos[p] == producto_encontrado:
            posicion_producto = p
            break

    if posicion_producto == -1:
        messagebox.showwarning("ERROR","No se encontro el producto asociado en el inventario")
        return

    try:
        partes=venta_texto.split("x")
        cantidad_comprada=int(partes[1].split()[0])
    except:
        cantidad_comprada=cantidad
    
    if cantidad > cantidad_comprada:
        messagebox.showwarning("ERROR", f"No puedes devolver {cantidad}. Solo compró {cantidad_comprada} unidad(es).")
        return
    elif cantidad < cantidad_comprada:
        stocks[posicion_producto]+=cantidad
        actualizado_cantidad=cantidad_comprada-cantidad
        actualizado_cantidad=str(actualizado_cantidad)
        venta_actualizado=venta_texto.replace(str(cantidad_comprada),actualizado_cantidad)
        ventas.pop(verificar)
        clientes_ventas.pop(verificar)
        ventas.insert(0,venta_actualizado)
        clientes_ventas.insert(0,cliente)
        movimientos.append(f"DEVOLUCIÓN PARCIAL ({cantidad}): {nombres_productos[posicion_producto]} DEL CLIENTE {cliente.upper()} | ATENDIÓ: {nombre.upper()}\n")
        guardar_datos()
        messagebox.showinfo("EXITO", "REEMBOLSO PARCIAL REGISTRADO Y STOCK ACTUALIZADO")
    if cantidad == cantidad_comprada:
        stocks[posicion_producto]+=cantidad
        ventas.pop(verificar)
        clientes_ventas.pop(verificar)
        movimientos.append(f"REEMBOLSO DEL PRODUCTO: {nombres_productos[posicion_producto]} DEL CLIENTE {cliente.upper()} QUE HIZO EL PERSONAL {nombre.upper()}\n ")
        guardar_datos()
        messagebox.showinfo("EXITO", "REEMBOLSO REGISTRADO Y STOCK ACTUALIZADO")
