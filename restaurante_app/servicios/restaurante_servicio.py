from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(self, datos_usuarios, datos_productos):
        self.usuarios = [Usuario(**dato) for dato in datos_usuarios]
        self.productos = [Producto(**dato) for dato in datos_productos]

    def validar_acceso(self, nombre_usuario, contrasena):
        nombre_usuario = nombre_usuario.strip()
        contrasena = contrasena.strip()

        if not nombre_usuario or not contrasena:
            return None

        for usuario in self.usuarios:
            if usuario.usuario == nombre_usuario and usuario.contrasena == contrasena:
                return usuario

        return None

    def listar_usuarios(self):
        return list(self.usuarios)

    def listar_productos(self):
        return list(self.productos)

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)
