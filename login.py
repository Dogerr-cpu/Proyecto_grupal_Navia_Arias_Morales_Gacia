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
