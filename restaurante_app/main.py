import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


BASE_DIR = Path(__file__).resolve().parent


class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("900x560")
        self.root.minsize(760, 480)

        self.restaurante_servicio = self._crear_servicio()
        self.vista_actual = None

        self.mostrar_login()

    def _crear_servicio(self):
        archivo_servicio = ArchivoServicio()

        datos_usuarios = archivo_servicio.leer_json(
            BASE_DIR / "datos" / "usuarios.json"
        )
        datos_productos = archivo_servicio.leer_json(
            BASE_DIR / "datos" / "productos.json"
        )

        return RestauranteServicio(datos_usuarios, datos_productos)

    def _cambiar_vista(self, nueva_vista):
        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_login(self):
        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )
        self._cambiar_vista(vista)

    def mostrar_principal(self, usuario):
        vista = MainView(
            self.root,
            self.restaurante_servicio,
            usuario,
            self.mostrar_login
        )
        self._cambiar_vista(vista)


def main():
    root = tk.Tk()
    RestauranteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
