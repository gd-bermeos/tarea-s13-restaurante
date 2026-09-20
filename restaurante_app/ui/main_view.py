import tkinter as tk
from tkinter import ttk


class MainView(ttk.Frame):
    def __init__(self, master, restaurante_servicio, usuario_actual, on_logout):
        super().__init__(master, padding=16)
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout

        self.producto_id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.mensaje_producto_var = tk.StringVar()
        self.tabla_productos = None

        self._construir_interfaz()
        self._mostrar_inicio()

    def _construir_interfaz(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 12))
        encabezado.columnconfigure(0, weight=1)

        ttk.Label(
            encabezado,
            text="Panel principal - Restaurante App",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(
            encabezado,
            text=f"Sesión: {self.usuario_actual.nombre} ({self.usuario_actual.rol})"
        ).grid(row=1, column=0, sticky="w", pady=(4, 0))

        ttk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.on_logout
        ).grid(row=0, column=1, rowspan=2, padx=(20, 0))

        menu = ttk.LabelFrame(self, text="Navegación", padding=10)
        menu.grid(row=1, column=0, sticky="ns", padx=(0, 12))

        ttk.Button(menu, text="Inicio", command=self._mostrar_inicio, width=20).pack(fill="x", pady=4)
        ttk.Button(menu, text="Productos", command=self._mostrar_productos, width=20).pack(fill="x", pady=4)
        ttk.Button(menu, text="Usuarios", command=self._mostrar_usuarios, width=20).pack(fill="x", pady=4)

        self.contenido = ttk.Frame(self, padding=6)
        self.contenido.grid(row=1, column=1, sticky="nsew")
        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(1, weight=1)

    def _limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def _mostrar_inicio(self):
        self._limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Resumen del sistema",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 15))

        resumen = (
            f"Productos registrados: {self.restaurante_servicio.cantidad_productos()}\n"
            f"Usuarios registrados: {self.restaurante_servicio.cantidad_usuarios()}\n\n"
            "Semana 14: componentes, contenedores y gestión de productos."
        )

        ttk.Label(
            self.contenido,
            text=resumen,
            font=("Arial", 11),
            justify="left"
        ).grid(row=1, column=0, sticky="nw")

    def _mostrar_productos(self):
        self._limpiar_contenido()
        self.contenido.rowconfigure(1, weight=1)

        ttk.Label(
            self.contenido,
            text="Gestión de productos",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        area = ttk.Frame(self.contenido)
        area.grid(row=1, column=0, sticky="nsew")
        area.columnconfigure(1, weight=1)
        area.rowconfigure(0, weight=1)

        formulario = ttk.LabelFrame(area, text="Formulario", padding=12)
        formulario.grid(row=0, column=0, sticky="ns", padx=(0, 12))

        campos = [
            ("ID:", self.producto_id_var),
            ("Nombre:", self.nombre_var),
            ("Categoría:", self.categoria_var),
            ("Precio:", self.precio_var),
            ("Cantidad:", self.cantidad_var)
        ]

        for fila, (texto, variable) in enumerate(campos):
            ttk.Label(formulario, text=texto).grid(row=fila, column=0, sticky="w", pady=5)
            ttk.Entry(formulario, textvariable=variable, width=24).grid(
                row=fila, column=1, sticky="ew", padx=(8, 0), pady=5
            )

        acciones = ttk.Frame(formulario)
        acciones.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        acciones.columnconfigure(0, weight=1)
        acciones.columnconfigure(1, weight=1)

        ttk.Button(
            acciones,
            text="Registrar",
            command=self._registrar_producto
        ).grid(row=0, column=0, sticky="ew", padx=(0, 4), pady=4)

        ttk.Button(
            acciones,
            text="Cargar / Consultar",
            command=self._cargar_producto
        ).grid(row=0, column=1, sticky="ew", padx=(4, 0), pady=4)

        ttk.Button(
            acciones,
            text="Actualizar",
            command=self._actualizar_producto
        ).grid(row=1, column=0, sticky="ew", padx=(0, 4), pady=4)

        ttk.Button(
            acciones,
            text="Eliminar",
            command=self._eliminar_producto
        ).grid(row=1, column=1, sticky="ew", padx=(4, 0), pady=4)

        ttk.Button(
            acciones,
            text="Limpiar formulario",
            command=self._limpiar_formulario
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(4, 0))

        ttk.Label(
            formulario,
            textvariable=self.mensaje_producto_var,
            wraplength=260,
            justify="left"
        ).grid(row=6, column=0, columnspan=2, sticky="w", pady=(12, 0))

        tabla_frame = ttk.LabelFrame(area, text="Productos registrados", padding=8)
        tabla_frame.grid(row=0, column=1, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)

        columnas = ("id", "nombre", "categoria", "precio", "cantidad")
        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=15
        )

        encabezados = {
            "id": "ID",
            "nombre": "Producto",
            "categoria": "Categoría",
            "precio": "Precio",
            "cantidad": "Cantidad"
        }
        anchos = {
            "id": 55,
            "nombre": 190,
            "categoria": 140,
            "precio": 90,
            "cantidad": 85
        }

        for columna in columnas:
            self.tabla_productos.heading(columna, text=encabezados[columna])
            self.tabla_productos.column(
                columna,
                width=anchos[columna],
                anchor="center"
            )

        scroll = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )
        self.tabla_productos.configure(yscrollcommand=scroll.set)

        self.tabla_productos.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")

        self._actualizar_tabla_productos()

    def _actualizar_tabla_productos(self):
        if self.tabla_productos is None:
            return

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        for producto in self.restaurante_servicio.listar_productos():
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.id,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.cantidad
                )
            )

    def _registrar_producto(self):
        try:
            producto = self.restaurante_servicio.registrar_producto(
                self.producto_id_var.get(),
                self.nombre_var.get(),
                self.categoria_var.get(),
                self.precio_var.get(),
                self.cantidad_var.get()
            )
            self.mensaje_producto_var.set(
                f"Producto '{producto.nombre}' registrado correctamente."
            )
            self._actualizar_tabla_productos()
            self._limpiar_campos()
        except ValueError as error:
            self.mensaje_producto_var.set(str(error))

    def _cargar_producto(self):
        try:
            producto = self.restaurante_servicio.buscar_producto(
                self.producto_id_var.get()
            )

            if producto is None:
                self.mensaje_producto_var.set("No se encontró un producto con ese ID.")
                return

            self.nombre_var.set(producto.nombre)
            self.categoria_var.set(producto.categoria)
            self.precio_var.set(str(producto.precio))
            self.cantidad_var.set(str(producto.cantidad))
            self.mensaje_producto_var.set(
                "Producto cargado. Puede actualizarlo o eliminarlo."
            )
        except ValueError as error:
            self.mensaje_producto_var.set(str(error))

    def _actualizar_producto(self):
        try:
            producto = self.restaurante_servicio.actualizar_producto(
                self.producto_id_var.get(),
                self.nombre_var.get(),
                self.categoria_var.get(),
                self.precio_var.get(),
                self.cantidad_var.get()
            )
            self.mensaje_producto_var.set(
                f"Producto '{producto.nombre}' actualizado correctamente."
            )
            self._actualizar_tabla_productos()
        except ValueError as error:
            self.mensaje_producto_var.set(str(error))

    def _eliminar_producto(self):
        try:
            producto = self.restaurante_servicio.eliminar_producto(
                self.producto_id_var.get()
            )
            self.mensaje_producto_var.set(
                f"Producto '{producto.nombre}' eliminado correctamente."
            )
            self._actualizar_tabla_productos()
            self._limpiar_campos()
        except ValueError as error:
            self.mensaje_producto_var.set(str(error))

    def _limpiar_formulario(self):
        self._limpiar_campos()
        self.mensaje_producto_var.set("")

    def _limpiar_campos(self):
        self.producto_id_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.cantidad_var.set("")

    def _mostrar_usuarios(self):
        self._limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        columnas = ("id", "nombre", "usuario", "rol")
        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings",
            height=14
        )

        encabezados = {
            "id": "ID",
            "nombre": "Nombre",
            "usuario": "Usuario",
            "rol": "Rol"
        }
        anchos = {
            "id": 60,
            "nombre": 240,
            "usuario": 180,
            "rol": 180
        }

        for columna in columnas:
            tabla.heading(columna, text=encabezados[columna])
            tabla.column(columna, width=anchos[columna], anchor="center")

        for usuario in self.restaurante_servicio.listar_usuarios():
            tabla.insert(
                "",
                tk.END,
                values=(usuario.id, usuario.nombre, usuario.usuario, usuario.rol)
            )

        tabla.grid(row=1, column=0, sticky="nsew")
