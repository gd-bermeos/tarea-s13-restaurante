import json
from pathlib import Path


class ArchivoServicio:
    @staticmethod
    def leer_json(ruta_archivo):
        ruta = Path(ruta_archivo)

        if not ruta.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError as error:
            raise ValueError(f"El archivo JSON no tiene un formato válido: {ruta}") from error
