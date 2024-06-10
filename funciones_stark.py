from os import system

def borrar_pantalla():
    """Borra la pantalla.
    """
    system("cls")

def pausar(): 
    """Pausa la iteracion para mostrar un dato en pantalla.
    """
    system("pause")

def validacion_letra(opcion: str)->str:
    """Valida que la opción ingresada se encunentre entre la opciones del menú

    Args:
        opcion (str): dato ingresado por el usuario de tipo string ingresado por el usuario

    Returns:
        str: caracter de tipo string validado
    """
    while opcion !='A' and opcion !='B' and opcion !=  'C' and opcion !='D' and opcion !='E' and opcion!='F' and opcion != 'G' and opcion != 'H' and opcion !='I' and opcion != 'J' and opcion != 'K' and opcion != 'L' and opcion != 'M' and opcion != 'N' and opcion != 'O' and opcion !='P':
        opcion = (input("Error. Vuela a ingresar una opción: ")).upper()
    return opcion

def menu_opciones()-> str:
    """muestra menú de opciones que el usuario deberá elegir

    Returns:
        str: _description_
    """
    borrar_pantalla()

    print("--MENU DE OPCIONES--")
    print ("A. Mostrar el nombre de cada superhéroe de género M")
    print ("B. Mostrar el nombre de cada superhéroe de género F")
    print ("C. Mostrar el superhéroe más alto de género M")
    print ("D. Mostrar el superhéroe más alto de género F")
    print ("E. Mostrar el superhéroe más bajo de género M")
    print ("F. Mostrar el superhéroe más bajo de género F")
    print ("G. Mostrar la altura promedio de los superhéroes de género M")
    print ("H. Mostrar la altura promedio de los superhéroes de género F")
    print ("I. Informar cual es el Nombre del superhéroe asociado a cada uno de los # indicadores anteriores (ítems C a F)")
    print ("J. Mostrar cuántos superhéroes tienen cada tipo de color de ojos.")
    print ("K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print ("L. Determinar cuántos superhéroes tienen cada tipo de inteligencia.")
    print ("M. Listar todos los superhéroes agrupados por color de ojos.")
    print("N. Listar todos los superhéroes agrupados por color de pelo.")
    print ("O. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print ("P - Salir")

    opcion = (input("Ingrese una opción: ")).upper()
    opcion = validacion_letra(opcion)

    return opcion

def filtrar_lista (filtradora, lista: list)->list:
    """filtra una lista de diccionarios según un criterio

    Args:
        filtradora (function): funcion lambda que filtra la lista por la condición deseada 
        lista (list): lista de diccionarios con datos

    Returns:
        list: lista de diccionarios filtrada según la condición deseada
    """
    lista_filtrada = []
    try: 
        for elemento in lista: 
            if filtradora(elemento):
                lista_filtrada.append(elemento)
        return lista_filtrada
    except ValueError:
        print("Lista vacía")

def mostrar_elemento_in_lista (lista:list) -> None:
    """muestra una lista de diccionarios por pantalla en forma de tabla

    Args:
        lista (list): _description_
    """
    mostrar_headline (lista)

    try:
        for elemento in lista: 
            mostrar_elemento(elemento)
    except ValueError: 
        print ("Lista vacía")

def mostrar_headline(lista: list)->None:
    """muestra el encabezado de una tabla de datos por pantalla en forma de columnas

    Args:
        lista (list): lista de diccionarios con datos 
    """
    try: 
        for key in lista[0].keys(): 
            print (f"{key:<21}", end = "")
        print (" ")
    except IndexError:
        print("Lista vacía")

def mostrar_elemento (diccionario: dict)->None: 
    """muestra la informacion de un diccionario desplegado en una fila

    Args:
        diccionario (dict): diccionario con datos
    """
    for value in diccionario.values():
        if len(str(value))<=18:
            print(f"{value:<21}", end= "")
        else: 
            print(f"{value:<30}", end= "")
    print (" ")

def mostrar_lista (lista: list) -> None:
    """muestra una lista por pantalla

    Args:
        lista (list): lista que se desea mostrar por pantalla
    """
    try: 
        for elemento in lista:
            print (elemento)
    except ValueError: 
        print("Lista vacía")

def mostrar_dict (diccionario: dict)->None:
    """muestra un diccionario por pantalla

    Args:
        diccionario (dict): diccionario que se desea mostrar
    """
    try: 
        for key, value in diccionario.items():
            print (key, value)
    except ValueError: 
        print("Diccionario vacío")

def mapear_lista (procesadora, lista: list)->list:
    """hace un proceso sobre una lista de entrada y 
        devuelve una lista de salida acorde al proceso realizado

    Args:
        procesadora (function): función lambda que contiene el proceso que se desea realizar
        lista (list): lista de entrada original

    Returns:
        list: lista de salida con un proceso realizado
    """
    
    lista_mapeada = []

    try: 
        for elemento in lista:
            lista_mapeada.append(procesadora(elemento))
        return lista_mapeada
    except ValueError: 
        print("Lista vacía")

def max_or_min_in_lista (reductora, lista:list)->dict:
    """muestra el elemento mámimo o mínimo de una lista

    Args:
        reductora (function): función lambda que evalúa si un valor es el máximo o mínimo
        lista (list): lista de entrada sin ningún procesamiento

    Returns:
        dict: diccionario de la lista con algún valor que cumple ser máximo o mínimo
    """
    try: 
        ant = lista[0]

        for act in lista[1:]:
            ant = reductora (ant, act)
        return ant 
    except IndexError: 
        print("Lista vacía")

def suma (lista: list)-> int: 
    """suma los elementos de tipo float o int de una lista y los acumula

    Args:
        lista (list): lista de entrada

    Returns:
        int: valor total de todos los datos numericos sumados
    """
    try:
        acumulador = 0

        for elemento in lista: 
            acumulador += elemento

        return acumulador
    except ValueError: 
        print("Lista vacía")

def promedio (lista:list)->float:
    """promedia los elementos de una lista

    Args:
        lista (list): lista de entrada

    Returns:
        int: promedio de los elementos sumados
    """
    try: 
        promedio = suma (lista) / len(lista)

        return promedio
    except ZeroDivisionError: 
        print ("No se puede dividir por cero")

def swap_lista (lista: list, i: int, j: int)-> None:
    """intercambia la posición de dos elementos de una lista

    Args:
        lista (list): lista de entraba
        i (int): elemento de la lista en la posición i 
        j (int): elemento de la lista en la posición j
    """
    aux = lista[i]
    lista[i] = lista [j]
    lista[j] = aux

def ordenar_full (criterio_ordenamiento, lista: list)->list:
    """ordena los elementos de una lista según un criterio

    Args:
        criterio_ordenamiento (function): función que indica según que criterio ordenar (asc o desc) y que valores comparar
        lista (list): lista de entrada

    Returns:
        list: devuelve la lista con los valores ordenados según un criterio
    """
    try: 
        for i in range (len(lista)-1):
            for j in range (i+1, len(lista)):
                if criterio_ordenamiento(lista[i], lista[j]):
                    swap_lista (lista, i, j)
        return lista
    except ValueError:
        print("Lista vacía")

def contar_x_criterio (criterio_conteo, lista: list)->dict:
    """cuenta los elementos de la lista según un valor especificado y los guarda en un diccionario de acuerdo a sus valores

    Args:
        criterio_conteo (function): función lambda que indica según que key hacer los contadores
        lista (list): lista de entrada

    Returns:
        dict: diccionario de contadores, cuya key es el valor de la lista de diccionarios de entrada
    """
    try:
        contadores = {}
        for elemento in lista: 

            value = criterio_conteo(elemento)

            if value == None or value == "":
                value = "No informa"

            if value in contadores: 
                contadores [value] += 1
            else: 
                contadores [value] = 1

        return contadores
    except ValueError: 
        "Lista vacía"
