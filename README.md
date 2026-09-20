# Restaurante App - Semana 14

## Descripción

Este proyecto corresponde a la **Semana 14** de Programación Orientada a Objetos y desarrolla el tema **Componentes y contenedores en Tkinter**.

La aplicación evoluciona la versión gráfica de la semana anterior sin reconstruir el proyecto desde cero. Se mantiene la arquitectura modular, el inicio de sesión, la consulta de usuarios y la persistencia en archivos JSON. La mejora principal se encuentra en la gestión de productos desde una interfaz organizada con formularios, botones, contenedores y una tabla de visualización.

## Estructura del proyecto

- restaurante_app/
  - datos/
    - productos.json
    - usuarios.json
  - modelos/
    - __init__.py
    - producto.py
    - usuario.py
  - servicios/
    - __init__.py
    - archivo_servicio.py
    - restaurante_servicio.py
  - ui/
    - __init__.py
    - login_view.py
    - main_view.py
  - main.py
- README.md

## Componentes y contenedores utilizados

La interfaz utiliza componentes de tkinter y ttk:

- Frame y LabelFrame para separar navegación, formulario y área de datos.
- Label para títulos, mensajes e información.
- Entry para ingresar los datos de productos y las credenciales.
- Button con command= para ejecutar las acciones.
- Treeview para presentar productos y usuarios en forma de tabla.
- Scrollbar para facilitar la visualización del listado de productos.
- Los gestores de geometría grid() y pack() para organizar los componentes.

## Mejoras realizadas en la Semana 14

- Se conserva el inicio de sesión gráfico.
- Se reorganiza la ventana principal mediante contenedores.
- Se mantiene una sección independiente para consultar usuarios.
- Se incorpora un formulario completo para gestionar productos.
- La tabla de productos se actualiza después de registrar, actualizar o eliminar.
- Las reglas y validaciones permanecen en RestauranteServicio.
- La lectura y escritura de JSON se mantiene en ArchivoServicio.
- No se utiliza edición directa de la tabla ni manejo avanzado de eventos.

## Operaciones de productos

Desde la sección **Productos** se pueden realizar las siguientes acciones:

1. **Registrar:** crea un producto nuevo si los datos son válidos y el ID no existe.
2. **Cargar / Consultar:** busca un producto por su ID y carga sus datos en el formulario.
3. **Actualizar:** modifica el producto identificado por el ID.
4. **Eliminar:** elimina el producto identificado por el ID.
5. **Limpiar formulario:** vacía los campos para una nueva operación.

Las validaciones controlan que el ID y la cantidad sean enteros válidos, que el precio sea numérico, que los valores no sean negativos y que nombre y categoría no estén vacíos.

## Persistencia

Los productos se almacenan en restaurante_app/datos/productos.json.

RestauranteServicio procesa las operaciones del dominio y solicita a ArchivoServicio guardar los cambios. De esta forma, la interfaz no lee ni escribe directamente el archivo JSON.

Los cambios realizados desde la aplicación se conservan al cerrar y volver a ejecutar el programa.

## Credenciales de prueba

| Usuario | Contraseña | Rol |
|---|---|---|
| admin | admin123 | Administrador |
| mesero | 1234 | Mesero |
| caja | caja123 | Cajero |

## Requisitos

- Python 3.10 o superior recomendado.
- Tkinter, incluido normalmente con Python en Windows.
- No se requieren librerías externas.

## Ejecución

1. Clone o descargue este repositorio.
2. Abra una terminal en la carpeta del proyecto.
3. Ingrese a la carpeta restaurante_app.
4. Ejecute: python main.py
5. En Windows también puede utilizar: py main.py

## Flujo general

Inicio de la aplicación → LoginView → validación mediante RestauranteServicio → MainView → Productos o Usuarios → acciones de productos → RestauranteServicio → ArchivoServicio → productos.json → actualización de la interfaz.

## Alcance académico

Esta versión está enfocada en **componentes y contenedores de Tkinter**. No implementa bases de datos, autenticación real, edición directa de tablas ni eventos avanzados de teclado, mouse o doble clic.
