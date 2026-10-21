usuarios_registrados=["sebas","gerson","camba"]
claves_registradas=["1234","abcd","1234"]
tipo_usuario=["administrador","usuario","comprador"]

def login(usuario,clave):
    for i in range(len(usuarios_registrados)):
        if usuarios_registrados[i] == usuario and claves_registradas[i] == clave:
            print("ACCESO CONCEDIDO")
            return tipo_usuario[i]
    return None

def ver_usuarios():
    for i in range(len(usuarios_registrados)):
        print(f"usuario: {usuarios_registrados[i]}: {tipo_usuario[i]}")

def agregar_usuario(usuario,clave,tipo):
    if tipo != "administrador" and tipo != "usuario" and tipo != "comprador":
        print("SOLO SE PUEDE ELEGIR ADMINISTRADOR, USUARIO O COMPRADOR")
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
        print(f"El usuario '{usuario}' fue eliminado exitosamente.")
    else:
        print("El usuario no existe en el sistema.")

def modificar_usuario(usuario):
    if usuario in usuarios_registrados:
        i = usuarios_registrados.index(usuario)
        print(f"Modificando al usuario: {usuario}")
        nueva_clave = input(f"Nueva clave (Actual: {claves_registradas[i]}): ")
        nuevo_tipo = input(f"Nuevo tipo (Actual: {tipo_usuario[i]}): ")
        if nueva_clave:
            claves_registradas[i] = nueva_clave    
        if nuevo_tipo:
            tipo_usuario[i] = nuevo_tipo
        print(f"¡Usuario '{usuario}' modificado exitosamente!")
    else:
        print("El usuario no existe en el sistema.")
