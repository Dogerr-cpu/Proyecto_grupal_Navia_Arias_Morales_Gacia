from inventario import ver_productos,agregar_producto,registrar_entrada,registrar_salida,ver_movimientos,ver_ventas
from login import ver_usuarios,agregar_usuario

def menu_administrador(nombre):
    while True:
        print(""" 
        1. Ver productos
        2. Agregar producto
        3. Registrar entrada
        4. Registrar salida
        5. Ver entradas y salidas
        6. Ver ventas
        7. Ver usuarios
        8. Agregar usuario
        9. Salir del sistema
        """)
        opcion=input("INGRESE UNA OPCION 1-9: ")
        if opcion == "1":
            ver_productos()
        elif opcion == "2":
            try:
                codigo=int(input("INGRESE EL CODIGO: "))
                nombre_producto=input("INGRESE EL NOMBRE: ").strip().lower()
                precio=int(input("INGRESE EL PRECIO: "))
                stock=int(input("INGRESE EL STOCK: "))
                agregar_producto(codigo,nombre_producto,precio,stock)
            except ValueError:
                print("===INGRESE NUMEROS ENTEROS===")
        elif opcion == "3":
            try:
                ver_productos()
                codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                cantidad=int(input("INGRESE LA CANTIDAD QUE ENTRA: "))
                registrar_entrada(codigo,cantidad,nombre)
            except ValueError:
                print("===INGRESE NUMEROS ENTEROS===")
        elif opcion == "4":
            try:
                ver_productos()
                codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                cantidad=int(input("INGRESE LA CANTIDAD QUE SALE: "))
                registrar_salida(codigo,cantidad,nombre)
            except ValueError:
                print("===INGRESE NUMEROS ENTEROS===")
        elif opcion == "5":
            ver_movimientos()
        elif opcion == "6":
            ver_ventas()
        elif opcion == "7":
            print("CARGANDO USUARIOS....")
            ver_usuarios()
        elif opcion == "8":
            print("CARGANDO SISTEMA...")
            usuario_nuevo=input("INGRESA UN USUARIO: ").strip().lower()
            clave_nueva=input(f"INGRESE LA CLAVE PARA {usuario_nuevo}: ")
            tipo_nuevo=input(f"INGRESE QUE ACCESOS QUIERE PARA {usuario_nuevo}: ").lower()
            agregar_usuario(usuario_nuevo,clave_nueva,tipo_nuevo)
        elif opcion == "9":
            print("SALIENDO DEL SISTEMA... ")
            break
        else:
            print("INGRESE UNA OPCION VALIDA")
