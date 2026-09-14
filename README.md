# Restaurante App - Semana 13

## Descripción

Este proyecto corresponde a la **Semana 13** de Programación Orientada a Objetos.
El objetivo es iniciar la transición de una aplicación de restaurante basada en consola
hacia una aplicación con **interfaz gráfica de usuario utilizando Tkinter**.

La versión implementada trabaja únicamente con **usuarios y productos**, conserva la
lectura de datos desde archivos JSON y separa las responsabilidades entre modelos,
servicios, interfaz gráfica y punto de entrada.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py

README.md
```

## Responsabilidades principales

- **Producto:** representa los productos disponibles en el restaurante.
- **Usuario:** representa los usuarios usados para la simulación de acceso.
- **ArchivoServicio:** lee los archivos JSON locales.
- **RestauranteServicio:** transforma los datos en objetos y concentra las operaciones de validación, listado y conteo.
- **LoginView:** muestra el formulario de acceso y solicita la validación al servicio.
- **MainView:** muestra el panel principal, productos, usuarios y la opción de ventas identificada como pendiente.
- **main.py:** crea una única ventana Tkinter, prepara las dependencias y controla el cambio entre LoginView y MainView.

## Flujo de la aplicación

```text
Inicio
  ↓
main.py carga JSON y prepara los servicios
  ↓
LoginView
  ↓
Validación mediante RestauranteServicio
  ↓
MainView
  ↓
Productos | Usuarios | Ventas (pendiente)
  ↓
Cerrar sesión
  ↓
LoginView
```

## Credenciales de prueba

| Usuario | Contraseña | Rol |
|---|---|---|
| admin | admin123 | Administrador |
| mesero | 1234 | Mesero |
| caja | caja123 | Cajero |

## Requisitos

- Python 3.10 o superior recomendado.
- Tkinter (incluido normalmente con Python en Windows).

No se necesitan librerías externas.

## Ejecución

1. Abra una terminal dentro de la carpeta del proyecto.
2. Ingrese a la carpeta `restaurante_app`.
3. Ejecute:

```bash
python main.py
```

En Windows también puede utilizar:

```bash
py main.py
```

## Funcionalidades implementadas

- Inicio de sesión gráfico.
- Validación de campos vacíos.
- Mensaje para credenciales incorrectas.
- Validación de acceso mediante `RestauranteServicio`.
- Visualización de productos cargados desde `productos.json`.
- Visualización de usuarios cargados desde `usuarios.json`.
- Conteo de productos y usuarios.
- Opción de ventas marcada como funcionalidad pendiente.
- Cierre de sesión sin abrir una segunda ventana.
- Una sola instancia de `Tk()` y un solo `mainloop()`.

## Observación

Esta versión es una base académica simplificada. No implementa autenticación segura,
bases de datos, ventas completas ni formularios avanzados, ya que esos elementos no
forman parte de los requisitos de la Semana 13.
