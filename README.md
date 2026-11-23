# Proyecto de Fundamentos de Programacion
Aquí estan los avances para el proyecto de Fundamentos de programación

# Simulador de Inventario (con metricas sobre el inventario)
- Puedes consultar el inventario que hay en una tienda (tu la administras, asi que puedes vender lo que quieras). Agregar productos, restarlos (por ventas, o alguna otro motivo), ver el precio de los productos, consultar cuantas unidades hay de cada producto, ademas de revisar el promedio, desviacion estándar y varianza de las unidades de el inventario.

- Pasos a seguir:
  Abrir un menu en el que se pregunte al usuario que quiere hacer: Si agregar productos (1), ver la lista de productos(2), calcular el cambio (3), hacer compras de los productos de el inventario (4) o cerrar el programa(5).
  - Si se elige 1: Agregar productos (con su precio) y guardarlos en un archivo de texto.
  - Si elige 2: Pedir el nombre de el producto y despliega el nombre con sus unidades.
  - Si elige 3: Pedir al usuario elegir un numero entero del 1 al 3 para poder mostrarle la varianza (1), el promedio (2) y la desviacion estandar (3) de todas las unidades en el inventario.
  - Si elige 4: Pide al usuario el nombre de el producto que quiere comprar (mostrándole la lista) y la cantidad que desea comprar. Resta la cantidad que acaba de comprar de la lista y no deja comprar mas de lo que ya tienes.
  - Si elige 5: Se cierra el programa.
  Una vez terminada cada accion, se muestra el menu al usuario.

# Librerias:
- Este proyecto utiliza la funcion "sleep()" (que funciona como un tiempo de suspensión) que viene de la libreria "time", ya incluida en el API de python.
- Ademas, utiliza la funcion "sqrt()" (recibe como parametro un numero y devuelve su raiz cuadrada) que viene de la libreria "math", tambien incluida en el API de python.

# Referencias consultadas para realizar el proyecto:
- Ortiz, A., & Martínez, Y. (s.f.). TC1028 Pensamiento computacional para ingeniería: Convenciones de estilo para Python.
- Python Software Foundation. (s. f.). Built-in types: str.rstrip. Python documentation. https://docs.python.org/3/library/stdtypes.html#str.rstrip
- Bala Priya C. (2022, 20 de octubre). Métodos de cadenas split() y join() en Python: Explicados con ejemplos. freeCodeCamp. https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/
- Python Guides. (s. f.). Print in the same line in Python. https://pythonguides.com/print-in-the-same-line-in-python/
- El Blog del Programador. (2026, 11 de octubre). Cómo imprimir en Python sin una nueva línea de forma controlada. https://elblogdelprogramador.com/posts/como-imprimir-en-python-sin-una-nueva-linea-de-forma-controlada/
# Referencias de las librerias:
- Python Software Foundation. (s. f.). *time — Funciones de tiempo y conversiones*. Documentación de Python. https://docs.python.org/es/3/library/time.html#time.sleep
- Python Software Foundation. (s. f.). *math — Funciones matemáticas*. Documentación de Python 3.10. https://docs.python.org/es/3.10/library/math.html#math.sqrt
