from inventario import ver_productos,vender,ver_mis_compras

def menu_comprador(nombre):
    while True:
        print(""" 
        1. Ver productos
        2. Comprar
        3. Ver mis compras
        4. Volver al login
        """)
        opcion=input("INGRESE UNA OPCION 1-4: ")
        match opcion:
            case "1":
                ver_productos()
            case "2":
                try:
                    ver_productos()
                    codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                    cantidad=int(input("INGRESE LA CANTIDAD: "))
                    vender(codigo,cantidad,nombre,nombre)
                except ValueError:
                    print("INGRESE NUMEROS ENTEROS")
            case "3":
                ver_mis_compras(nombre)
            case "4":
                print("CERRANDO SESION....")
                break
            case _:
                print("INGRESE UNA OPCION VALIDA")
