usuarios_registrados=["sebas","gerson","camba"]
claves_registradas=["1234","abcd","1234"]
tipo_usuario=["administrador","vendedor","comprador"]

def login(usuario,clave):
    for i in range(len(usuarios_registrados)):
        if usuarios_registrados[i] == usuario and claves_registradas[i] == clave:
            print("ACCESO CONCEDIDO")
            return tipo_usuario[i]
    return None

def ver_usuarios():
    for i in range(len(usuarios_registrados)):
        print(f"USUARIO: {usuarios_registrados[i].upper()}: {tipo_usuario[i].upper()}")

def agregar_usuario(usuario,clave,tipo):
    if tipo != "administrador" and tipo != "vendedor" and tipo != "comprador":
        print("SOLO SE PUEDE ELEGIR ADMINISTRADOR, VENDEDOR O COMPRADOR")
    elif usuario in usuarios_registrados:
        print("ESE USUARIO YA EXISTE")
    else:
        usuarios_registrados.append(usuario)
        claves_registradas.append(clave)
        tipo_usuario.append(tipo)
        print("CUENTA AGREGADA")

def eliminar_usuario(usuario):
    if usuario in usuarios_registrados:
        i = usuarios_registrados.index(usuario)
        del usuarios_registrados[i]
        del claves_registradas[i]
        del tipo_usuario[i]
        print(f"EL USUARIO '{usuario.upper()}' FUE ELIMINADO EXITOSAMENTE.")
    else:
        print("EL USUARIO NO EXISTE EN EL SISTEMA.")

def modificar_usuario(usuario):
    if usuario in usuarios_registrados:
        i = usuarios_registrados.index(usuario)
        print(f"MODIFICANDO AL USUARIO: {usuario.upper()}")
        nueva_clave = input(f"NUEVA CLAVE (ACTUAL: {claves_registradas[i]}): ").strip()
        nuevo_tipo = input(f"NUEVO TIPO (ACTUAL: {tipo_usuario[i].upper()}): ").strip().lower()
        if nueva_clave:
            claves_registradas[i] = nueva_clave
        if nuevo_tipo:
            if nuevo_tipo == "administrador" or nuevo_tipo == "vendedor" or nuevo_tipo == "comprador":
                tipo_usuario[i] = nuevo_tipo
            else:
                print("TIPO INVALIDO, SE MANTUVO EL TIPO ANTERIOR")
        print(f"¡USUARIO '{usuario.upper()}' MODIFICADO EXITOSAMENTE!")
    else:
        print("EL USUARIO NO EXISTE EN EL SISTEMA.")
