class Producto:
    def __init__(self, id, nombre, categoria, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def __str__(self):
        return (
            f"{self.nombre} | {self.categoria} | "
            f"${self.precio:.2f} | Stock: {self.cantidad}"
        )
