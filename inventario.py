def menu(pregunta):

    """Desde aqui se accede a todas las funciones que puede
        hacer el programa"""

    # Crea el archivo
    with open('Lista.txt', 'w') as archivo_creado:
        archivo_creado.close()

    if pregunta == 3:
        print("Escribe el dinero recibido: ")
        cambio = float(input())
        print("Escribe el precio: ")
        precio = float(input())
        return calcula_cambio(cambio, precio, pregunta)
    
    elif pregunta == 5:
        print("Hasta Luego!!")
        exit()
        
    elif pregunta == 4:
        # Abre el archivo, pero solo lee y muestra la lista
        with open("Lista.txt", "r") as iniciar_compra:
            print("Busca que lo que vas a comprar a continuacion: ")
            # lee todas las lineas al abrirlo
            lineas_archivo = iniciar_compra.readlines()
        
            # Mostramos el inventario actual
            for linea in lineas_archivo:
                print(linea.strip())

        print("Escribe el nombre de lo que quieres comprar: ")
        producto = input()
        print("Escribe la cantidad de producto: ")
        cantidad_compra = int(input())
        
        # Usa la lista ya leida, el producto y la cantidad
        return comprar(
            lineas_archivo, producto, cantidad_compra, pregunta
        )

    elif pregunta == 2:
        buscar_producto = input("Escribe el nombre del producto"
                                " que quieres encontrar: ")
        return listado(buscar_producto, pregunta)

    elif pregunta == 1:
        agregar_producto = input("Escribe el nombre de el producto "
                                 "que quieres agregar: ")
        return agregador(agregar_producto, pregunta)

    return pregunta


# funciones
def agregador(agregar_producto, pregunta):

    """Se encarga de agregar el nombre de el producto que pone
        el usuario, con la cantidad de este mismo"""

    print("Escribe la cantidad: ")
    cantidad = int(input())
    prod_y_cant = f"{agregar_producto}-{cantidad}\n"
    with open("Lista.txt", "a") as escribir_producto:
        escribir_producto.write(prod_y_cant)
    print("Acabas de registrar",
                "'" + agregar_producto + "'", "con", cantidad, 
                 "unidades. Cerrando el programa"
                 " para guardar cambios...")
    return menu(5)


def listado(buscar_producto, pregunta):

    """Muestra todos los productos en la lista que
       coinciden con la busqueda del usuario"""

    print('Resultados: ')
    design = '---------------------------'
    print(design)
    evita_error = open("Lista.txt", "a")
    evita_error.close()
    with open("Lista.txt", "r") as leer:
        for renglon in leer:
            if buscar_producto in renglon:
                mostrar = renglon.strip()
                print(mostrar)
                break
    print("----Fin de los resultados---")

    while True:
        print("Encontraste lo que buscabas? si (1), para no (2)")
        encontro_producto = int(input())
        if encontro_producto == 1:
            print("Me alegro! Regresando al menu...")
            return pregunta
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

    # Logica similar a la funcion que enlista, solo que ahora si con listas
    nueva_lista = []
    encontrado = False
    producto_suficiente = True

    for prods in lineas_archivo:
        if producto in prods:
            encontrado = True
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
                nuevo_renglon = f"{producto}-{nueva_cantidad}\n"
                nueva_lista.append(nuevo_renglon)
        else:
            nueva_lista.append(prods)

    if not encontrado:
        print("El producto que escribiste no existe en la lista.", 
               "Agregalo desde la opcion 1 del menu.")
        return pregunta

    # Solo guarda cambios en el archivo si habia suficiente producto
    elif producto_suficiente:
        with open("Lista.txt", "w") as archivo_escribir:
            archivo_escribir.writelines(nueva_lista)

    return pregunta


def calcula_cambio(cambio, precio, pregunta):

    """Calcula el cambio a partir de dos entradas: 
        El dinero recibido y el dinero a devolver."""
    
    if cambio < precio:
        print("DINERO INSUFICIENTE")
        return pregunta
    else:
        print(f"El cambio es: {cambio - precio}")
        return pregunta


# Controla la entrada de menu
while True:
    print("Agregar nuevos productos(1), vender(2), "
        "calcular el cambio (3), comprar (4) o salir (5)?:"
           )
    print("Escribe 1, 2, 3, 4 o 5: ")
    
    pregunta = int(input())
    
    # Valida el numero:

    if pregunta not in [1, 2, 3, 4, 5]:
        print("Escribe solo del 1 al 5")
    else:
        # Se envia la pregunta al menu. Cuando la funcion termine
        # El ciclo empieza de nuevo, y reinicia la pregunta
        menu(pregunta)def menu(pregunta):

    """Desde aqui se accede a todas las funciones que puede
        hacer el programa"""

    # Crea el archivo
    with open('Lista.txt', 'w') as archivo_creado:
        archivo_creado.close()

    if pregunta == 3:
        print("Escribe el dinero recibido: ")
        cambio = float(input())
        print("Escribe el precio: ")
        precio = float(input())
        return calcula_cambio(cambio, precio, pregunta)
    
    elif pregunta == 5:
        print("Hasta Luego!!")
        exit()
        
    elif pregunta == 4:
        # Abre el archivo, pero solo lee y muestra la lista
        with open("Lista.txt", "r") as iniciar_compra:
            print("Busca que lo que vas a comprar a continuacion: ")
            # lee todas las lineas al abrirlo
            lineas_archivo = iniciar_compra.readlines()
        
            # Mostramos el inventario actual
            for linea in lineas_archivo:
                print(linea.strip())

        print("Escribe el nombre de lo que quieres comprar: ")
        producto = input()
        print("Escribe la cantidad de producto: ")
        cantidad_compra = int(input())
        
        # Usa la lista ya leida, el producto y la cantidad
        return comprar(
            lineas_archivo, producto, cantidad_compra, pregunta
        )

    elif pregunta == 2:
        buscar_producto = input("Escribe el nombre del producto"
                                " que quieres encontrar: ")
        return listado(buscar_producto, pregunta)

    elif pregunta == 1:
        agregar_producto = input("Escribe el nombre de el producto "
                                 "que quieres agregar: ")
        return agregador(agregar_producto, pregunta)

    return pregunta


# funciones
def agregador(agregar_producto, pregunta):

    """Se encarga de agregar el nombre de el producto que pone
        el usuario, con la cantidad de este mismo"""

    print("Escribe la cantidad: ")
    cantidad = int(input())
    prod_y_cant = f"{agregar_producto}-{cantidad}\n"
    with open("Lista.txt", "a") as escribir_producto:
        escribir_producto.write(prod_y_cant)
    print("Acabas de registrar",
                "'" + agregar_producto + "'", "con", cantidad, 
                 "unidades. Cerrando el programa"
                 " para guardar cambios...")
    return menu(5)


def listado(buscar_producto, pregunta):

    """Muestra todos los productos en la lista que
       coinciden con la busqueda del usuario"""

    print('Resultados: ')
    design = '---------------------------'
    print(design)
    evita_error = open("Lista.txt", "a")
    evita_error.close()
    with open("Lista.txt", "r") as leer:
        for renglon in leer:
            if buscar_producto in renglon:
                mostrar = renglon.strip()
                print(mostrar)
                break
    print("----Fin de los resultados---")

    while True:
        print("Encontraste lo que buscabas? si (1), para no (2)")
        encontro_producto = int(input())
        if encontro_producto == 1:
            print("Me alegro! Regresando al menu...")
            return pregunta
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

    # Logica similar a la funcion que enlista, solo que ahora si con listas
    nueva_lista = []
    encontrado = False
    producto_suficiente = True

    for prods in lineas_archivo:
        if producto in prods:
            encontrado = True
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
                nuevo_renglon = f"{producto}-{nueva_cantidad}\n"
                nueva_lista.append(nuevo_renglon)
        else:
            nueva_lista.append(prods)

    if not encontrado:
        print("El producto que escribiste no existe en la lista.", 
               "Agregalo desde la opcion 1 del menu.")
        return pregunta

    # Solo guarda cambios en el archivo si habia suficiente producto
    elif producto_suficiente:
        with open("Lista.txt", "w") as archivo_escribir:
            archivo_escribir.writelines(nueva_lista)

    return pregunta


def calcula_cambio(cambio, precio, pregunta):

    """Calcula el cambio a partir de dos entradas: 
        El dinero recibido y el dinero a devolver."""
    
    if cambio < precio:
        print("DINERO INSUFICIENTE")
        return pregunta
    else:
        print(f"El cambio es: {cambio - precio}")
        return pregunta


# Controla la entrada de menu
while True:
    print("Agregar nuevos productos(1), vender(2), "
        "calcular el cambio (3), comprar (4) o salir (5)?:"
           )
    print("Escribe 1, 2, 3, 4 o 5: ")
    
    pregunta = int(input())
    
    # Valida el numero:

    if pregunta not in [1, 2, 3, 4, 5]:
        print("Escribe solo del 1 al 5")
    else:
        # Se envia la pregunta al menu. Cuando la funcion termine
        # El ciclo empieza de nuevo, y reinicia la pregunta
        menu(pregunta)
