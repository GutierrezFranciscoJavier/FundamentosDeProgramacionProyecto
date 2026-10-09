# Menu. Llama a todas las funciones.
def menu(pregunta):
    """Desde aqui se accede a todas las funciones que puede
       hacer el programa"""
    if pregunta == 3:
        print("Escribe el dinero recibido: ")
        num1 = float(input())
        print("Escribe el precio: ")
        num2 = float(input())
        return calcula_cambio(num1, num2)
    
    elif pregunta == 5:
        print("Hasta Luego!!")
        exit()
        
    elif pregunta == 4:
        # Abre el archivo. solo lee y muestra la lista
        iniciar_compra = open("Lista.txt", "r")
        print("Busca que lo que vas a comprar: ")
        #.readlines() lee todas las lineas del open()
        lineas_archivo = iniciar_compra.readlines()
        
        # Mostramos el inventario actual
        for linea in lineas_archivo:
            print(linea.strip())
        iniciar_compra.close()

        print("Escribe el nombre de lo que quieres comprar: ")
        producto = input()
        print("Escribe la cantidad de producto: ")
        cantidad_compra = int(input())
        
        # Usa la lista ya leida,
        # el producto y la cantidad
        return comprar(lineas_archivo, producto, cantidad_compra, pregunta)

    elif pregunta == 2:
        buscar_producto = input("Escribe el nombre del producto"
                        " que quieres encontrar: ")
        return lista(buscar_producto)

    elif pregunta == 1:
        agregar_producto = input("Escribe el nombre de el producto "
                                "que quieres agregar: ")
        return agregador(agregar_producto)

    return pregunta


# funciones
def agregador(agregar_producto, menu):
    """Se encarga de agregar el nombre de el producto que pone
       el usuario, con la cantidad de este mismo"""
    
    escribir_producto = open("Lista.txt", "a")
    print("Escribe la cantidad: ")
    cantidad = int(input())

    prod_y_cant = f"{agregar_producto}-{cantidad}-unidades.\n"
    escribir_producto.write(prod_y_cant)
    print("Acabas de registrar",
                "'"+ agregar_producto +"'", "con", cantidad, 
                 "unidades. Cerrando el programa"
                 " para guardar cambios...")
    return menu(5)


def lista(producto, pregunta):
    """ "evita_error" crea una lista
    (si es que se seleccionara)
    el 2 en el menu y no hubiera una lista creada."""

    print('Resultados: ')
    design = '---------------------------'
    print(design)
    evita_error = open("Lista.txt", "a")
    evita_error.close()
    with open("Lista.txt", "r") as leer:
        for renglon in leer:
            if producto in renglon:
                mostrar = renglon.strip()
                print(mostrar)
                break
    print("----Fin de los resultados---")

    while True:
            print("Encontraste lo que buscabas? si (1), para no (2)")
            encontro_producto = int(input())

            if encontro_producto != 1 and encontro_producto != 2:
                print('Escribe solo 1 o 2.')
            else:
                print('Usa la opcion 1 para agregarlo,'
                ' y lo puedes comprar desde la opcion 4')
                print(design)
                return pregunta


def comprar(lineas_archivo, producto, cantidad_compra, pregunta):
    """El usuario elige de que producto se va a sustraer
       la cantidad de su preferencia, se refleja al instante"""

    # Logica similar a def lista(), solo que ahora si con listas
    nueva_lista = []
    encontrado = False
    producto_suficiente = True

    for prods in lineas_archivo:
        if producto in prods:
            encontrado = True

            """Esto quita los "-" con los que separa las unidades 
            del nombre el agregador... Pense en usar
            expresiones regulares (con la libreria 're'), tal vez
            la use mas adelante"""

            partes = prods.strip().split("-")
            # Convierte los digitos en enteros
            cantidad_actual = int(partes[1])
            
            # Verifica si hay esas unidades a la venta
            if cantidad_compra > cantidad_actual:
                print(f"No puedes comprar tanto!,Solo quedan "
                      f"{cantidad_actual} unidades.")
                producto_suficiente = False
                # Aqui la linea queda como si nada
                nueva_lista.append(prods)
            else:
                # Se hace la resta
                nueva_cantidad = cantidad_actual - cantidad_compra
                print(f"Compraste '{producto}', tenias "
                      f"{cantidad_actual} y ahora"
                      f" tienes {nueva_cantidad} unidades.")
                
                #Se escribe sin la cantidad restada
                nuevo_renglon = f"{producto}-{nueva_cantidad}-\
                    unidades.\n"
                nueva_lista.append(nuevo_renglon)
        else:
            nueva_lista.append(prods)

    if not encontrado:
        print("El producto que escribiste no existe en la lista.")
        return pregunta

    # Solo guarda cambios en el archivo si habia suficiente producto
    elif producto_suficiente:
        # "w" solo escribe
        archivo_escribir = open("Lista.txt", "w")
        # es como ".readlines()", pero este escribe
        archivo_escribir.writelines(nueva_lista)
        archivo_escribir.close()

    return pregunta


def calcula_cambio(cambio, precio, pregunta):

    """Calcula el cambio a partir de dos entradas: 
       El dinero recibido y el dinero a devolver."""
    
    if cambio < precio:
        print("DINERO INSUFICIENTE")
        return pregunta
    else:
        mensaje = print(f"El cambio es: {cambio - precio}")
        return mensaje, pregunta

# Controla la entrada de menu
while True:
    print("Agregar nuevos productos(1), vender(2), "
        "calcular el cambio (3), comprar (4) o salir (5)?:"
           )
    print("Escribe 1, 2, 3, 4 o 5: ")
    
    pregunta = int(input())
    
    # Valida el numero:

    if (pregunta != 1 and pregunta != 2 and pregunta != 3 and
        pregunta != 4 and pregunta != 5):
        print("Escribe solo del 1 al 5")
    else:
# Se envia la pregunta al menu. Cuando la funcion termine
# El while empieza de nuevo, y reinicia la pregunta
        menu(pregunta) 
