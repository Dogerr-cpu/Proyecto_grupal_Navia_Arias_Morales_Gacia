from login import login
from admin import menu_administrador
from usuario import menu_usuario
from comprador import menu_comprador

def main():
    while True:
        print("===BIENVENIDO A LA TIENDA DE COMPUTADORAS===")
        print(""" 
        1. INICIAR SESION
        2. SALIR DEL PROGRAMA
        """)
        opcion=input("INGRESE UNA OPCION 1-2: ")
        if opcion == "1":
            usuario_ingresado=input("INGRESE UN USUARIO: ").strip().lower()
            clave_ingresada=input("INGRESE SU CONTRASEÑA: ").strip()
            tipo=login(usuario_ingresado,clave_ingresada)

            if tipo == "administrador":
                print(f"===BIENVENIDO AL MENU DE {tipo.upper()}===")
                menu_administrador(usuario_ingresado)
            elif tipo == "usuario":
                print(f"===BIENVENIDO AL MENU DE {tipo.upper()}===")
                menu_usuario(usuario_ingresado)
            elif tipo == "comprador":
                print(f"===BIENVENIDO AL MENU DE {tipo.upper()}===")
                menu_comprador(usuario_ingresado)
            else:
                print("USUARIO O CONTRASEÑA INVALIDO")
        elif opcion == "2":
            print("SALIENDO DEL PROGRAMA....")
            break
        else:
            print("INGRESE UNA OPCION VALIDA")

main()
