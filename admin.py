from inventario import ver_productos,agregar_producto,registrar_entrada,registrar_salida,ver_movimientos,ver_ventas
from login import ver_usuarios,agregar_usuario, eliminar_usuario, modificar_usuario
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
        9. Eliminar usuario
        10. Modificar usuario
        11. Salir del sistema
        """)
        opcion=input("INGRESE UNA OPCION 1-11: ")
        
        match opcion:
            case "1":
                ver_productos()
            case "2":
                try:
                    codigo=int(input("INGRESE EL CODIGO: "))
                    nombre_producto=input("INGRESE EL NOMBRE: ").strip().lower()
                    if nombre_producto.replace(" ","").isalpha():
                        precio=int(input("INGRESE EL PRECIO DEL PRODUCTO ($): "))
                        stock=int(input("INGRESE EL STOCK: "))
                        agregar_producto(codigo,nombre_producto,precio,stock)
                    else:
                        print("NO PUEDES PONER NUMEROS EN NOMBRE DEL PRODUCTO")
                except ValueError:
                    print("===INGRESE NUMEROS ENTEROS===")
            case "3":
                try:
                    ver_productos()
                    codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                    cantidad=int(input("INGRESE LA CANTIDAD QUE ENTRA: "))
                    registrar_entrada(codigo,cantidad,nombre)
                except ValueError:
                    print("===INGRESE NUMEROS ENTEROS===")
            case "4":
                try:
                    ver_productos()
                    codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
                    cantidad=int(input("INGRESE LA CANTIDAD QUE SALE: "))
                    registrar_salida(codigo,cantidad,nombre)
                except ValueError:
                    print("===INGRESE NUMEROS ENTEROS===")
            case "5":
                ver_movimientos()
            case "6":
                ver_ventas()
            case "7":
                print("CARGANDO USUARIOS....")
                ver_usuarios()
            case "8":
                print("CARGANDO SISTEMA...")
                usuario_nuevo=input("INGRESA UN USUARIO: ").strip().lower()
                clave_nueva=input(f"INGRESE LA CLAVE PARA {usuario_nuevo}: ")
                tipo_nuevo=input(f"INGRESE QUE ACCESOS QUIERE PARA {usuario_nuevo}: ").lower()
                agregar_usuario(usuario_nuevo,clave_nueva,tipo_nuevo)
            case "9":
                usuario_eliminar=input("ingrese el usuario a eliminar: ").lower().strip()
                eliminar_usuario(usuario_eliminar)
            case "10":
                usuario_modificar=input("INGRESE EL USUARIO QUE DESEA CAMBIAR SU CONTRASEÑA: ").lower().strip()
                modificar_usuario(usuario_modificar)
            case "11":
                print("CERRANDO SESION")
                from main import main
                main()
            case _:
                print("INGRESE UNA OPCION VALIDA")