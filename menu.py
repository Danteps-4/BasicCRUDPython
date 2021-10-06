from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

opcion = None

while opcion != 5:
    print("Opciones".center(20, "-"))
    print("1- Listar usuarios")
    print("2- Agregar usuario")
    print("3- Actualizar usuario")
    print("4- Eliminar usuario")
    print("5- Salir")

    try:
        opcion = int(input("Ingrese su opcion: "))
    except Exception as e:
        print(f"Ingrese una opcion valida: {e}")

    if opcion == 1:
        print("Listando usuarios".center(20, "-"))
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            print(usuario)
    elif opcion == 2:
        username = input("Ingrese un username: ")
        password = input("Ingrese un password: ")
        usuario = Usuario(username=username, password=password)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        print(f"Usuarios insertados: {usuario_insertado}")
    elif opcion == 3:
        id_usuario = int(input("Ingrese el id_usuario: "))
        username = input("Ingrese el nuevo username: ")
        password = input("Ingrese el nuevo password: ")
        usuario = Usuario(id_usuario, username, password)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        print(f"Usuarios actualizados: {usuario_actualizado}")
    elif opcion == 4:
        id_usuario = int(input("Ingrese el id_usuario a eliminar: "))
        usuario = Usuario(id_usuario=id_usuario)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        print(f"Usuarios eliminados: {usuario_eliminado}")

print("Saliendo de la aplicacion")