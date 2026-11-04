codigos=[1,2,3]
nombres_productos=["laptop","mouse","teclado"]
precios=[12000,250,600]
stocks=[5,20,10]

movimientos=[]
ventas=[]
clientes_ventas=[]

def ver_productos():
    print("="*50)
    print("PRODUCTOS DISPONIBLES")
    print("="*50)
    for i in range(len(codigos)):
        print(f"CODIGO {codigos[i]}: {nombres_productos[i]:<10} | PRECIO DOLARES: {precios[i]:<10}$ | PRECIO BS: {precios[i]*12:<10.2f} BS | STOCK: {stocks[i]}")

def buscar_producto(codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1

def agregar_producto(codigo,nombre,precio,stock):
    if buscar_producto(codigo) != -1:
        print("ESE CODIGO YA EXISTE")
    elif precio <= 0 or stock < 0:
        print("INGRESE DATOS VALIDOS")
    else:
        codigos.append(codigo)
        nombres_productos.append(nombre)
        precios.append(precio)
        stocks.append(stock)
        print("PRODUCTO AGREGADO")

def registrar_entrada(codigo,cantidad,responsable):
    posicion=buscar_producto(codigo)
    if posicion == -1:
        print("PRODUCTO NO ENCONTRADO")
    elif cantidad <= 0:
        print("INGRESE UNA CANTIDAD VALIDA")
    else:
        stocks[posicion]=stocks[posicion]+cantidad
        movimientos.append(f"ENTRADA - {nombres_productos[posicion]:<8} | CANTIDAD: {cantidad:<5} | POR: {responsable}")
        print("ENTRADA REGISTRADA")

def registrar_salida(codigo,cantidad,responsable):
    posicion=buscar_producto(codigo)
    if posicion == -1:
        print("PRODUCTO NO ENCONTRADO")
    elif cantidad <= 0:
        print("INGRESE UNA CANTIDAD VALIDA")
    elif cantidad > stocks[posicion]:
        print("NO HAY SUFICIENTE STOCK")
    else:
        stocks[posicion]=stocks[posicion]-cantidad
        movimientos.append(f"SALIDA - {nombres_productos[posicion]:<8} | CANTIDAD: {cantidad:<5} | POR: {responsable}")
        print("SALIDA REGISTRADA")

def vender(codigo,cantidad,cliente,vendedor):
    posicion=buscar_producto(codigo)
    if posicion == -1:
        print("PRODUCTO NO ENCONTRADO")
    elif cantidad <= 0:
        print("INGRESE UNA CANTIDAD VALIDA")
    elif cantidad > stocks[posicion]:
        print("NO HAY SUFICIENTE STOCK")
    else:
        total=precios[posicion]*cantidad
        stocks[posicion]=stocks[posicion]-cantidad
        ventas.append(f"{nombres_productos[posicion]} x {cantidad} = ${total} - CLIENTE: {cliente}")
        clientes_ventas.append(cliente)
        movimientos.append(f"SALIDA (VENTA) - {nombres_productos[posicion]} - CANTIDAD: {cantidad} - POR: {vendedor}")
        print(f"VENTA REALIZADA. TOTAL: ${total}")

def ver_movimientos():
    print("="*50)
    print("ENTRADAS Y SALIDAS")
    print("="*50)
    for movimiento in movimientos:
        print(movimiento)

def ver_ventas():
    print("="*50)
    print("VENTAS REALIZADAS")
    print("="*50)
    for venta in ventas:
        print(venta)

def ver_mis_compras(cliente):
    print("="*50)
    print("MIS COMPRAS")
    print("="*50)
    for i in range(len(ventas)):
        if clientes_ventas[i] == cliente:
            print(ventas[i])