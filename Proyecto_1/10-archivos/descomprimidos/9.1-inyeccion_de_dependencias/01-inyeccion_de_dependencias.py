import usuario
import usuario_2

def guardar():               #esta no tiene inyeccion de dependencias porque es exclusiva de usuario, y al querer usar otra clase no podria
    usuario.guardar()

def guardar_inyeccion(entidad):    #Esta es una inyeccion de dependencias para poder por ejemplo usar el metodo con otra clase. ejemplo abajo
        entidad.guardar()


guardar()

guardar_inyeccion(usuario)
guardar_inyeccion(usuario_2)
