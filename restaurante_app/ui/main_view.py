import tkinter as tk
from tkinter import ttk


class MainView(ttk.Frame):
    def __init__(self, master, restaurante_servicio, usuario_actual, on_logout):
        super().__init__(master, padding=20)
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout

        self._construir_interfaz()
        self._mostrar_inicio()

    def _construir_interfaz(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 15))
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

        menu = ttk.Frame(self)
        menu.grid(row=1, column=0, sticky="ns", padx=(0, 15))

        ttk.Button(menu, text="Inicio", command=self._mostrar_inicio, width=20).pack(fill="x", pady=4)
        ttk.Button(menu, text="Productos", command=self._mostrar_productos, width=20).pack(fill="x", pady=4)
        ttk.Button(menu, text="Usuarios", command=self._mostrar_usuarios, width=20).pack(fill="x", pady=4)
        ttk.Button(
            menu,
            text="Ventas (pendiente)",
            command=self._mostrar_ventas_pendientes,
            width=20
        ).pack(fill="x", pady=4)

        self.contenido = ttk.Frame(self, padding=10)
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
            "Esta versión corresponde a la base gráfica de la Semana 13."
        )

        ttk.Label(
            self.contenido,
            text=resumen,
            font=("Arial", 11),
            justify="left"
        ).grid(row=1, column=0, sticky="nw")

    def _mostrar_productos(self):
        self._limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Productos registrados",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        columnas = ("id", "nombre", "categoria", "precio", "cantidad")
        tabla = ttk.Treeview(self.contenido, columns=columnas, show="headings", height=12)

        encabezados = {
            "id": "ID",
            "nombre": "Producto",
            "categoria": "Categoría",
            "precio": "Precio",
            "cantidad": "Cantidad"
        }
        anchos = {"id": 60, "nombre": 200, "categoria": 150, "precio": 100, "cantidad": 100}

        for columna in columnas:
            tabla.heading(columna, text=encabezados[columna])
            tabla.column(columna, width=anchos[columna], anchor="center")

        for producto in self.restaurante_servicio.listar_productos():
            tabla.insert(
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

        tabla.grid(row=1, column=0, sticky="nsew")

    def _mostrar_usuarios(self):
        self._limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        columnas = ("id", "nombre", "usuario", "rol")
        tabla = ttk.Treeview(self.contenido, columns=columnas, show="headings", height=12)

        encabezados = {
            "id": "ID",
            "nombre": "Nombre",
            "usuario": "Usuario",
            "rol": "Rol"
        }
        anchos = {"id": 60, "nombre": 220, "usuario": 160, "rol": 160}

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

    def _mostrar_ventas_pendientes(self):
        self._limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Ventas",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        ttk.Label(
            self.contenido,
            text=(
                "Funcionalidad pendiente.\n"
                "Se incorporará en una etapa posterior del proyecto."
            ),
            font=("Arial", 11),
            justify="left"
        ).grid(row=1, column=0, sticky="nw")
