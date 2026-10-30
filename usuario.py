from inventario import ver_productos,vender,registrar_entrada,registrar_salida,ver_movimientos,ver_ventas

def menu_usuario(nombre):
    while True:
        print(""" 
        1. Ver productos
        2. Vender
        3. Registrar entrada
        4. Registrar salida
        5. Ver entradas y salidas
        6. Ver ventas
        7. Volver al login
        """)
        opcion=input("INGRESE UNA OPCION 1-7: ")
        match opcion:
            case "1":
                ver_productos()
            case "2":
                try:
                    ver_productos()
                    cliente=input("INGRESE EL NOMBRE DEL CLIENTE: ").strip().lower()
                    if cliente.isalpha():
                        codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                        cantidad=int(input("INGRESE LA CANTIDAD: "))
                        vender(codigo,cantidad,cliente,nombre)
                    else:
                        print("NO SE DEBE PONER NUMEROS EN EL NOMBRE DEL CLIENTE")
                except ValueError:
                    print("INGRESE NUMEROS ENTEROS")
            case "3":
                try:
                    ver_productos()
                    codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                    cantidad=int(input("INGRESE LA CANTIDAD QUE ENTRA: "))
                    registrar_entrada(codigo,cantidad,nombre)
                except ValueError:
                    print("INGRESE NUMEROS ENTEROS")
            case "4":
                try:
                    ver_productos()
                    codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                    cantidad=int(input("INGRESE LA CANTIDAD QUE SALE: "))
                    registrar_salida(codigo,cantidad,nombre)
                except ValueError:
                    print("INGRESE NUMEROS ENTEROS")
            case "5":
                ver_movimientos()
            case "6":
                ver_ventas()
            case "7":
                print("CERRANDO SESIÓN....")
                break
            case _:
                print("INGRESE UNA OPCION VALIDA")
