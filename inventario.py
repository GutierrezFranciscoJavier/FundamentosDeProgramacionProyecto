# Variables
SEPARADOR = '---------------------------'

# funciones
def pedir_nombre(mensaje):

    """
    Esta funcion hace que al recibir un nombre, nunca se pueda quedar vacio
    """

    nombre = input(mensaje).strip()

    while nombre == "":
        print("Debes escribir algo...")
        nombre = input(mensaje).strip()

    return nombre


def pedir_cantidad(mensaje):

    """Pide una cantidad entera mayor que cero. Usado por todas las funciones
       que necesitan manipular numeros."""

    cantidad = int(input(mensaje))

    while cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        cantidad = int(input(mensaje))

    return cantidad


def cargar_inventario():

    """Toma el archivo y recorre cada una de sus lineas
       y agrega tanto el nombre como la cantidad a una lista dentro
       de la lista inventario"""

    inventario = []

    with open("Lista.txt", "a"):
        print("Cargando Inventario...")

    with open("Lista.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            # Para indexar nombre y cantidad solamente
            datos = linea.split("-")

            nombre = datos[0].strip()
            cantidad_texto = datos[1].strip()

            inventario.append([nombre, int(cantidad_texto)])
    return inventario


def guardar_inventario(inventario):

    """Guarda cada producto y su cantidad en el archivo."""

    with open("Lista.txt", "w") as archivo:
        for producto in inventario:
            archivo.write(f"{producto[0]}-{producto[1]}\n")


def agregador(nombre, cantidad):

    """Agrega un producto o suma unidades si ya está registrado.
       Hace todo minusculas y asi compara 
       la entrada vs lo que hay en la lista"""

    inventario = cargar_inventario()
    encontrado = False
    indice = 0

    while indice < len(inventario) and not encontrado: 
        if inventario[indice][0].lower() == nombre.lower():
            inventario[indice][1] += cantidad
            encontrado = True
        indice += 1

    if not encontrado:
        inventario.append([nombre, cantidad])

    guardar_inventario(inventario)

    return f"Acabas de registrar {nombre}, con {cantidad} unidades."


def comprar(nombre, cantidad):

    """Resta del inventario las unidades compradas, si hay suficientes"""

    inventario = cargar_inventario()
    nombre_buscado = nombre.strip().lower()

    for producto in inventario:
        nombre_producto = producto[0]

        if nombre_producto.strip().lower() == nombre_buscado:
            cantidad_actual = producto[1]

            if cantidad > cantidad_actual:
                return f"Compra {cantidad_actual} unidades o menos!"

            producto[1] -= cantidad
            guardar_inventario(inventario)
            return (
                f"Compraste {cantidad} unidades de '{nombre_producto}'. "
                f"Quedan {producto[1]}."
            )

    return f"No existe el producto '{nombre}'."


def buscar_producto(nombre):

    """
    Busca coincidencias en los nombres de los productos, 
    donde no importa si esta en minusculas o mayusculas
    """
    
    inventario_listo = cargar_inventario()
    resultados = []

    for producto in inventario_listo:
        if nombre.lower() in producto[0].lower():
            resultados.append(
                f"{producto[0]}: {producto[1]} unidades"
            )

    if len(resultados) == 0:
        return "No se encontraron productos con ese nombre."
    return "Resultados:\n" + SEPARADOR + "\n" + "\n".join(resultados)


def mostrar_inventario():

    """Devuelve el inventario en forma de texto."""

    inventario = cargar_inventario()
    resultados = []

    for producto in inventario:
        resultados.append(f"{producto[0]}: {producto[1]} unidades")

    if len(resultados) == 0:
        return "El inventario está vacío."

    return "Inventario:\n" + SEPARADOR + "\n" + "\n".join(resultados)


def pedir_dinero(mensaje):

    """Pide una cantidad de dinero que no sea negativa.
       Muy parecida a pedir"""
    
    cantidad = float(input(mensaje))

    while cantidad < 0:
        print("La cantidad no puede ser negativa.")
        cantidad = float(input(mensaje))
    return cantidad


def calcular_cambio(dinero, precio):
    """Calcula el cambio o informa si el dinero no es suficiente."""
    if dinero < precio:
        return "DINERO INSUFICIENTE."

    cambio = dinero - precio
    return f"El cambio es: {cambio:.2f}"


def menu(pregunta):
    
    """Desde aqui se accede a todas las funciones que puede
        hacer el programa a traves de lo recibido en pregunta"""

    if pregunta == 1:
        nombre = pedir_nombre("Escribe el nombre del producto: ")
        cantidad = pedir_cantidad("Escribe la cantidad: ")
        print(agregador(nombre, cantidad))

    elif pregunta == 2:
        nombre = pedir_nombre("Escribe el producto que buscas: ")
        print(buscar_producto(nombre))

    elif pregunta == 3:
        dinero = pedir_dinero("Escribe el dinero recibido: ")
        precio = pedir_dinero("Escribe el precio: ")
        print(calcular_cambio(dinero, precio))

    elif pregunta == 4:
        print(mostrar_inventario())
        nombre = pedir_nombre("Escribe el producto que quieres comprar: ")
        cantidad = pedir_cantidad("Escribe la cantidad que quieres comprar: ")
        print(comprar(nombre, cantidad))


# Parte principal de el programa
pregunta = 0

while pregunta != 5:
    print("\nAgregar producto (1), buscar (2), calcular cambio (3) "
            "comprar (4) o salir (5).")
    pregunta = int(input("Escribe una opción del 1 al 5: "))

    if pregunta >= 1 and pregunta <= 4:
        menu(pregunta)
    elif pregunta != 5:
        print("Escribe solo una opción del 1 al 5.")

print("Hasta luego!")
