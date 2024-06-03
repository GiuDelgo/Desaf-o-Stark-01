from funciones_stark import *
from data_stark import lista_personajes

while True: 
    match (menu_opciones()):
        case "A":
            # A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            heroes_m_nombre = mapear_lista (lambda elemento: elemento ["nombre"], filtrar_lista(lambda elemento: elemento["genero"] == "M", lista_personajes))
            mostrar_lista (heroes_m_nombre)
        case "B":
            # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            heroes_f_nombre = mapear_lista (lambda elemento: elemento ["nombre"], filtrar_lista(lambda elemento: elemento["genero"] == "F", lista_personajes))
            mostrar_lista (heroes_f_nombre)
        case "C":
            # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            heroe_m_max_altura = max_or_min_in_lista (lambda ant, act: ant if ant["altura"] > act["altura"] else act, filtrar_lista(lambda elemento: elemento["genero"] == "M", lista_personajes))
            try: 
                print (f"{heroe_m_max_altura['nombre']} es el superhéroes más alto con {heroe_m_max_altura['altura']} mts")
            except TypeError: 
                print("")
        case "D":
            # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            heroe_f_max_altura = max_or_min_in_lista (lambda ant, act: ant if ant["altura"] > act["altura"] else act, filtrar_lista(lambda elemento: elemento["genero"] == "F", lista_personajes))
            try: 
                print (f"{heroe_f_max_altura['nombre']} es la superheroína más alta con {heroe_f_max_altura['altura']} mts")
            except TypeError: 
                print("") 
        case "E":
            # E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            heroe_m_min_altura = max_or_min_in_lista (lambda ant, act: ant if ant["altura"] < act["altura"] else act, filtrar_lista(lambda elemento: elemento["genero"] == "M", lista_personajes))
            try: 
                print (f"{heroe_m_min_altura['nombre']} es el superhéroes más bajo con {heroe_m_min_altura['altura']} mts")
            except TypeError: 
                print("") 
        case "F":
            # F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            heroe_f_min_altura = max_or_min_in_lista (lambda ant, act: ant if ant["altura"] < act["altura"] else act, filtrar_lista(lambda elemento: elemento["genero"] == "F", lista_personajes))
            try:
                print (f"{heroe_f_min_altura['nombre']} es la superheroína más baja con {heroe_f_min_altura['altura']} mts")
            except TypeError: 
                print("") 
        case "G":
            # G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            promedio_m_altura = promedio(mapear_lista(lambda elemento: elemento ["altura"], filtrar_lista(lambda elemento: elemento["genero"] == "M", lista_personajes)))
            print (f"El promedio de altura de los superhéroes masculinos es {promedio_m_altura} mts")
        case "H":
            # H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
            promedio_f_altura = promedio(mapear_lista(lambda elemento: elemento ["altura"], filtrar_lista(lambda elemento: elemento["genero"] == "F", lista_personajes)))
            print (f"El promedio de altura de los superhéroes femeninos es {promedio_f_altura} mts")
        case "I":
            # I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            heroe_m_max_altura = max_or_min_in_lista (lambda ant, act: ant if ant["altura"] > act["altura"] else act, filtrar_lista(lambda elemento: elemento["genero"] == "M", lista_personajes))
            try:
                print (f"El superhéroe más alto es {heroe_m_max_altura['nombre']}")
            except TypeError: 
                print("") 
            heroe_f_max_altura = max_or_min_in_lista (lambda ant, act: ant if ant["altura"] > act["altura"] else act, filtrar_lista(lambda elemento: elemento["genero"] == "F", lista_personajes))
            
            try:   
                print (f"La superheroína más es {heroe_f_max_altura['nombre']}")
            except TypeError: 
                print("") 
        case "J":
            # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            mostrar_dict (contar_x_criterio(lambda elemento: elemento["color_ojos"], lista_personajes))
        case "K":
            # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            mostrar_dict (contar_x_criterio(lambda elemento: elemento["color_pelo"], lista_personajes))
        case "L":
            # L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
            mostrar_dict (contar_x_criterio(lambda elemento: elemento["inteligencia"], lista_personajes))
        case "M":
            # M. Listar todos los superhéroes agrupados por color de ojos.
            lista_ordenada_color_ojos = ordenar_full (lambda elemento_i, elemento_j: elemento_i ["color_ojos"] > elemento_j ["color_ojos"], lista_personajes)
            mostrar_elemento_in_lista(lista_ordenada_color_ojos)
        case "N":
            # N. Listar todos los superhéroes agrupados por color de pelo.
            lista_ordenada_color_pelo = ordenar_full (lambda elemento_i, elemento_j: elemento_i ["color_pelo"] > elemento_j ["color_pelo"], lista_personajes)
            mostrar_elemento_in_lista(lista_ordenada_color_pelo)
        case "O":
            # O. Listar todos los superhéroes agrupados por tipo de inteligencia
            lista_ordenada_inteligencia = ordenar_full (lambda elemento_i, elemento_j: elemento_i ["inteligencia"] > elemento_j ["inteligencia"], lista_personajes)
            mostrar_elemento_in_lista(lista_ordenada_inteligencia)
        case "P":
            salir = input("Seguro que desea salir? Ingrese SI o NO: ")
            while salir.lower() != "si" and salir.lower() != "no":
                salir = input("Opcion incorrecta. Seguro que desea salir? Ingrese SI o NO: ")
            if salir == "si":
                print ("--------FIN DEL PROGRAMA---------")
                break
            else: 
                continue
    pausar()

