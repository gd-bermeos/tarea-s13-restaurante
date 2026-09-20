from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(
        self,
        datos_usuarios,
        datos_productos,
        archivo_servicio=None,
        ruta_productos=None
    ):
        self.usuarios = [Usuario(**dato) for dato in datos_usuarios]
        self.productos = [Producto(**dato) for dato in datos_productos]
        self.archivo_servicio = archivo_servicio
        self.ruta_productos = ruta_productos

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

    def buscar_producto(self, producto_id):
        producto_id = self._validar_id(producto_id)

        for producto in self.productos:
            if producto.id == producto_id:
                return producto

        return None

    def registrar_producto(self, producto_id, nombre, categoria, precio, cantidad):
        producto_id, nombre, categoria, precio, cantidad = self._validar_datos_producto(
            producto_id, nombre, categoria, precio, cantidad
        )

        if self.buscar_producto(producto_id) is not None:
            raise ValueError("Ya existe un producto con ese ID.")

        producto = Producto(
            producto_id,
            nombre,
            categoria,
            precio,
            cantidad
        )
        self.productos.append(producto)
        self._guardar_productos()
        return producto

    def actualizar_producto(self, producto_id, nombre, categoria, precio, cantidad):
        producto_id, nombre, categoria, precio, cantidad = self._validar_datos_producto(
            producto_id, nombre, categoria, precio, cantidad
        )

        producto = self.buscar_producto(producto_id)
        if producto is None:
            raise ValueError("No se encontró un producto con ese ID.")

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.cantidad = cantidad

        self._guardar_productos()
        return producto

    def eliminar_producto(self, producto_id):
        producto_id = self._validar_id(producto_id)
        producto = self.buscar_producto(producto_id)

        if producto is None:
            raise ValueError("No se encontró un producto con ese ID.")

        self.productos.remove(producto)
        self._guardar_productos()
        return producto

    @staticmethod
    def _validar_id(producto_id):
        try:
            producto_id = int(producto_id)
        except (TypeError, ValueError) as error:
            raise ValueError("El ID debe ser un número entero.") from error

        if producto_id <= 0:
            raise ValueError("El ID debe ser mayor que cero.")

        return producto_id

    def _validar_datos_producto(self, producto_id, nombre, categoria, precio, cantidad):
        producto_id = self._validar_id(producto_id)
        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not nombre:
            raise ValueError("Ingrese el nombre del producto.")

        if not categoria:
            raise ValueError("Ingrese la categoría del producto.")

        try:
            precio = float(precio)
        except (TypeError, ValueError) as error:
            raise ValueError("El precio debe ser un número válido.") from error

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError) as error:
            raise ValueError("La cantidad debe ser un número entero.") from error

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        return producto_id, nombre, categoria, precio, cantidad

    def _guardar_productos(self):
        if self.archivo_servicio is None or self.ruta_productos is None:
            raise ValueError("No se configuró la persistencia de productos.")

        datos = [
            {
                "id": producto.id,
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            }
            for producto in self.productos
        ]

        self.archivo_servicio.guardar_json(self.ruta_productos, datos)
