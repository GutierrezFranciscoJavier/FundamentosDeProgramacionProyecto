# Librerias
import time
import math

# Variables
SEPARADOR = '---------------------------'

# funciones
def disenio(texto, signo, tiempo):

    """
    Recibe: Una cadena de texto que varia entre funciones para mostrarlo en la
    pantalla de carga, los signos (que son una cadena de texto)
    que se agregan conforme el tiempo y recibe un entero
    (el tiempo) que es manipulado por la funcion para tener el tiempo 
    con el que aparecen los signos

    Utiliza time para que, dado un texto y un tiempo, muestre un simbolo
    uno tras otro en una misma linea (a modo de "pantalla de carga").

    Devuelve: La cadena texto con los signos siendo agregados con el tiempo
    """

    for vueltas in range(6):
        print(texto+(signo*vueltas), end='\r')
        operacion = (tiempo*vueltas)/0.89
        time.sleep(operacion)


def pedir_nombre(mensaje):

    """
    Recibe: una cadena de texto que varia entre funciones 

    Esta funcion hace que al recibir un nombre, nunca se pueda quedar vacio
    
    Devuelve: El nombre sin espacios al inicio y al final de la cadena 
    """

    nombre = input(mensaje).strip()

    while nombre == "":
        print("Debes escribir algo")
        nombre = input(mensaje).strip()

    return nombre


def pedir_cantidad(mensaje):

    """
    Recibe: Un mensaje para colocarlo en el input de la peticion de cantidad.
    
    Usado por todas las funciones que necesitan manipular numeros.

    Devuelve: Un numero entero
    """

    cantidad = int(input(mensaje))

    while cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        cantidad = int(input(mensaje))

    return cantidad


def guardar_inventario(inventario):

    """
    Recibe: La matriz del inventario

    Guarda cada producto registrado en la funcion agregador
    su nombre y su cantidad de unidades en el archivo.
    """

    disenio("Guardando Inventario", "~", 0.28)
    with open("Lista.txt", "w") as archivo:
        for producto in inventario:
            archivo.write(f"{producto[0]}-{producto[1]}\n")


def cargar_inventario():

    """
    Toma el archivo y recorre cada una de sus lineas y agrega
    tanto el nombre como la cantidad a una lista dentro
    de la lista inventario

    Devuelve: El inventario en forma de matriz
    """

    inventario = []

    with open("Lista.txt", "a"):
        disenio("Abriendo Inventario",".", 0.04)

    with open("Lista.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            # Para indexar nombre y cantidad solamente
            datos = linea.split("-")

            nombre = datos[0].strip()
            cantidad_texto = datos[1].strip()

            inventario.append([nombre, int(cantidad_texto)])
    return inventario


def agregador(nombre, cantidad):

    """
    Recibe: una cadena de texto dada por el usuario que debe incluir el nombre
    de un producto y un entero que debe incluir la cantidad de unidades de
    el producto que escribe en la cadena.

    Agrega un producto o suma unidades si ya está registrado.
    Hace todo minusculas y asi compara la entrada vs lo que hay en la lista

    Devuele: Una cadena te texto que indica el nombre del producto
    y las unidades agregadas
    """

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

    """
    Recibe: nombre (una cadena de texto dada por el usuario)
    cantidad (un entero dado por el usuario)

    Busca el nombre y si se encuentra en el inventario y resta las
    las unidades escritas en cantidad (si hay suficientes)

    Devuelve: Una cadena de texto que confirma los cambios realizados
    """

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
    Recibe: nombre del producto (string ingrsado por el usuario)

    Busca coincidencias en los nombres de los productos, 
    donde no importa si esta en minusculas o mayusculas
    y los guarda en una lista

    Devuelve: la en forma de cadena con un formato estetico
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
    return "\nResultados:\n" + SEPARADOR + "\n" + "\n".join(resultados)


def mostrar_inventario():

    """
    Usa la funcion cargar_inventario y desarma el inventario para mostrarlo
    en la forma de cadena de texto

    Devuelve: el inventario en forma de texto.
    """

    inventario = cargar_inventario()
    resultados = []

    for producto in inventario:
        resultados.append(f"{producto[0]}: {producto[1]} unidades")

    if len(resultados) == 0:
        return "El inventario está vacío."

    return "\nInventario:\n" + SEPARADOR + "\n" + "\n".join(resultados)


def promedio():

    """
    Usa la funcion cargar_inventario para tomar los valores de las unidades
    en la matriz y los suma, donde tambien lleva la cuenta de los productos
    recorridos

    Devuelve: El valor numerico del promedio (entero o flotante)
    """

    inventario = cargar_inventario()
    suma = 0
    productos_en_total = 0

    for producto in inventario:
            suma += producto[1]
            productos_en_total += 1
    
    prom = suma/productos_en_total

    return prom


def varianza():

    """
    Toma la funcion promedio y cargar_inventario para 
    calcular la varianza entre la cantidad del producto
    que evalua y el promedio

    Devuelve: La varianza en formato numerico (entero o flotante)
    """
    inventario = cargar_inventario()
    media = promedio()
    resultados_resta = 0
    total_datos = 0

    for productos in inventario:
        operacion = productos[1]-media
        al_cuadrado = operacion*operacion
        resultados_resta += al_cuadrado
        total_datos += 1

    varianza_unidades = resultados_resta/total_datos

    return varianza_unidades


def desv_estandar():

    """

    Utiliza la funcion varianza para calcular la desviacion estandar y aplica
    una raiz cuadrada sobre ese resultado para obtener la desviacion estandar

    Devuelve: La desviacion estandar calculada (solo con cuatro decimales)
    """

    varianza_inventario = varianza()
    desviacion_estandar = math.sqrt(varianza_inventario)

    return f'{desviacion_estandar:.4f}'

def calculos(cantidad):

    """  
    Recibe: cantidad (entero que representa la opcion elegida por el usuario)

    Esta funcion manda a llamar a la funcionalidad elegida por el usuario
    Puede entenderse como un sub-menu

    Devuelve: la varianza, el promedio o la desviacion estandar de las
    unidades de todo lo que se encuentre dentro del inventario

    """

    resultado_media = promedio()
    resultado_varianza = varianza()

    if cantidad == 1:
        return f'La varianza en inventario es de: {varianza()}'
    elif cantidad == 2:
        return f'El promedio de unidades en inventario es de: {promedio()}'
    elif cantidad == 3:
        return f'La desviacion estandar en inventario es: {desv_estandar()}'
    

def menu(pregunta):
    
    """
    Recibe: pregunta (Entero que controla las distintas opciones del programa)

    Desde aqui se accede a todas las funciones que puede
    hacer el programa a traves de lo recibido en pregunta

    Devuelve: Una funcion de acuerdo a el numero seleccionado en pregunta
    """

    if pregunta == 1:
        disenio("Abriendo agregador", ".", 0.07)
        nombre = pedir_nombre("Escribe el nombre del producto: ")
        cantidad = pedir_cantidad("Escribe la cantidad: ")
        print(agregador(nombre, cantidad))

    elif pregunta == 2:
        disenio("Abriendo buscador", ".", 0.07)
        nombre = pedir_nombre("Escribe el producto que buscas: ")
        print(buscar_producto(nombre))

    elif pregunta == 3:
        disenio("Abriendo calculos", ".", 0.07)
        cantidad = pedir_cantidad(
            "Mostrar varianza en el inventario (1), "+
            "Mostrar promedio de unidades en el inventario (2), "+
            "Mostrar desviacion estandar de unidades en el inventario (3): ")

        # Revisa que se eligan las opciones definidas
        while cantidad != 1 and cantidad != 2 and cantidad != 3:
            cantidad = pedir_cantidad("Solo puedes escoger (1), (2) o (3): ")

        print(calculos(cantidad))

    elif pregunta == 4:
        disenio("Abriendo compras", ".", 0.07)
        print(mostrar_inventario())
        nombre = pedir_nombre("Escribe el producto que quieres comprar: ")
        cantidad = pedir_cantidad("Escribe la cantidad que quieres comprar: ")
        print(comprar(nombre, cantidad))


# Parte principal de el programa

pregunta = 0

while pregunta != 5:
    print("\nAgregar producto (1), Buscar (2),"+
            "Estadísticas de el inventario (3),"+
            " Comprar (4) o salir (5).")
    pregunta = int(input("Escribe una opción del 1 al 5: "))

    if pregunta >= 1 and pregunta <= 4:
        menu(pregunta)
    elif pregunta != 5:
        print("Escribe solo una opción del 1 al 5.")

print("Hasta luego!")
disenio("Cerrando", ".", 0.05)
