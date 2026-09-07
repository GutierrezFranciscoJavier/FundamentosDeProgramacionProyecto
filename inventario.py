# funciones

def agregador():
    agregar_producto = input("Escribe el nombre de el producto que quieres agregar: ")

    escribir_producto = open("Lista.txt", "a")
    print("Escribe la cantidad: ")
    cantidad = int(input())

        # Pone el nombre del prodcuto y la cantidad en una sola línea

    producto_y_cantidad = f"{agregar_producto} tienes {cantidad} unidades.\n"
    escribir_producto.write(producto_y_cantidad)

        # Muestra al usuario lo que se registró en el archivo

    return print("Acabas de resigstrar", "'"+ agregar_producto +"'", "con", cantidad, 
                 "unidades. Cerrando el programa para guardar cambios..."), exit()

# Falta encontrar una mejor manera de conocer los elementos de el Inventario y para restar las cantidades solicitadas

# Por ahora esta es mi solución:

def lista(buscar_producto, pregunta_encontro_producto, pregunta_vender, pregunta_escoger_vender):
    with open("Lista.txt", "r") as leer:

        encontrado = False
        for renglon in leer:
            if buscar_producto in renglon:
                # print(renglon.strip())
                solo_unidades = renglon.strip(buscar_producto)
                print(solo_unidades)
                encontrado = True
                if encontrado == True:
                    break

        encontro_producto = input(pregunta_encontro_producto)

        if encontro_producto == "1":
            escoger_vender = input(pregunta_escoger_vender)
            if escoger_vender == "1":
                escoger_vender = (pregunta_vender)
                return print("Todavía estoy trabajando en una solución para vender :)")

            """ restando_cantidad = buscar_producto - vender
                if vender is not>= buscar_producto
                    return print("No tienes esa cantidad de unidades") """

            if escoger_vender == "2":
                return print("Trata escribiendo bien, o no lo sé!"), menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)

def calculadora(num1, num2, operacion):
    if operacion == 1:
        return print(f"tu resultado es:  {num1 + num2}"), menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)
    
    elif operacion == 2:
        return print(f" tu resultado es: {num1 * num2}"), menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)
    
    elif operacion == 3:
        return print(f" tu resultado es: {num1 - num2}"), menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)
    
    elif operacion == 4:
        if num2 == 0:
            return print("No puedes dividir entre cero. "), menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)
        return print(f" tu resultado es: {num1 / num2}"), menu(pregunta_texto, pregunta_buscar_prod,
        pregunta_encontro_producto, pregunta_vender,
        pregunta_escoger_vender)

# Menú. Llama a todas las funciones.


def menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender):
    pregunta = input(pregunta_texto)
    if pregunta == "3":
        num1 = float(input("Escribe el primer número de la operación: "))
        num2 = float(input("Escribe el segundo número de la operación: "))
        operacion = float(input("Escribe (1) para sumar, (2) para multiplicar, (3) para restar, (4) para dividir: "))
        return calculadora(num1, num2,operacion)
    
    elif pregunta == "4":
        print("Hasta Luego!!")
        exit()

    elif pregunta == "2":
        buscar_producto = input(pregunta_buscar_prod)
        return lista(buscar_producto,pregunta_encontro_producto,
                    pregunta_vender, pregunta_escoger_vender)

    elif pregunta == "1":
        return agregador()

    print("Escribe solo 1, 2, 3 o 4")
    return menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)


pregunta_texto = (
    "Quieres agregar nuevos productos(1), vender(2), usar una calculadora (3) o salir (4)?: "
    "Escribe 1, 2, 3 o 4: "
)

pregunta_buscar_prod = (
    "Escribe el nombre del producto que quieres encontrar: "
)

pregunta_encontro_producto = (
    "Encontraste lo que busacabas? sí (1), para no (2):"
)
pregunta_vender = (
    "Cuantas unidades te gustaría vender?:"
)
pregunta_vender = (
    "Cuantas unidades te gustaría vender?:"
)
pregunta_escoger_vender = (
    "Te gustría vender? sí (1), no (2)"
)

menu(pregunta_texto, pregunta_buscar_prod,
pregunta_encontro_producto, pregunta_vender,
pregunta_escoger_vender)
