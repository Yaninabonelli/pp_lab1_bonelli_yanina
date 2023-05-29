from Parcial.biblioteca_calculos import*
import re

def menu_de_opciones()->int:
    '''
    No recibe nada
    Muestra menú con opciones, valida input
    Devuelve un int de la opcion igresada
    '''
    opcion_correcta = False

    while opcion_correcta == False:
        
        respuesta_txt = input("\n      Menú de opciones:    \n1-Ver Jugadores\n2-Ver estadisticas por jugador\n3-Exportar estadisticas a CSV\n4-Ver logros por jugador\n5-Mostrar promedios de puntos por partido\n6-Consultar si es miembro del Salón de la Fama del Baloncesto\n7-Mostrar jugador con mayor cant de rebotes totales\n8-Mostrar jugador con mayor porcentaje de tiros de campo\n9-Mostrar jugador con mayor cantidad de asistencias totales\n10-Mostrar jugadores que han promediado más puntos por partido en relación a un valor determinado\n11-Mostrar jugadores que han promediado más rebotes en relación a un valor determinado\n12-Mostrar jugadores que han promediado más asistencias en relación a un valor determinado\n13-Mostrar jugador con mayor cant de robos totales\n14-Mostrar jugador con mayor cant de bloqueos totales\n15-Mostrar jugadores con porcentaje de tiros libres mayor a un valor determinado\n16-Mostrar promedios de puntos por partido, excluyendo al de menor cantidad\n17-Mostrar jugador con mayor cant de logros obtenidos\n18-Mostrar jugadores con porcentaje de tiros triples mayor a un valor determinado\n19-Mostrar jugador con mayor cant de temporadas jugadas\n20-Mostrar jugadores con porcentaje de tiros de campo mayor a un valor determinado ordenados\n21-Bonus\n22-Salir del programa\n\n")
           
        if re.match(r'^[0-9]{1,2}$',respuesta_txt) and int(respuesta_txt) >= 1 and int(respuesta_txt) <=24:
            respuesta = int(respuesta_txt)
            opcion_correcta = True
        else:
            print("Ingrese una opción valida.")
    
    return respuesta

def mostrar_jugadores(lista:list,key:str,texto:str):
    '''
    Recibe una lista, una key y un texto
    Muestra los datos recibidos como parámetros
    No devuelve nada
    '''
    if len(lista) >= 1:
        for jugador in lista:
            print("Nombre: {0} - {1}: {2}".format(jugador['nombre'],texto,jugador['posicion']))
    
    
def mostrar_datos_por_indice(lista:list)->list:
    '''
    Recibe una lista como parámetro
    Pide dato y valida para los datos del indice elegido
    Devuelve lista con la información del personaje, -1 si la lista está vacía
    '''
    opcion_correcta = False
    lista_nueva = []
    diccionario_nuevo = {}    
    
    if len(lista) >=1:

        while opcion_correcta == False:    
            respuesta_txt = input("Ingrese un jugador:\n0-Micheael Jordan\n1-Magic Johnson\n2-Larry Bird\n3-Charles Barkley\n4-Scottie Pipen\n5-David Robinson\n6-Patrik Ewing\n7-Karl Malone\n8-John Sctockton\n9-Clayde Drexler\n10-Chris Mullin\n11-Chrstian Leattner\n")

            if re.search(r'^[0-9]{1,2}$',respuesta_txt) and int(respuesta_txt) >=0 and int(respuesta_txt) <=11:
                respuesta_int = int(respuesta_txt)
                
                for indice in range(len(lista)):
                    if  indice == respuesta_int:
                        diccionario_nuevo['nombre'] = lista[indice]['nombre']
                        diccionario_nuevo['estadisticas'] = lista[indice]['estadisticas']
                        lista_nueva.append(diccionario_nuevo)    
                        opcion_correcta = True    
                        print(lista_nueva) 
                        return lista_nueva
            else:
                print("Los numeros ingresados son inconrrectos")
    else:
        print("La lista está vacía ")
        return -1
    
    
    
def buscar_jugador()->str:
    '''
    No recibe nada
    Solicita dato y valida
    Devuelve el dato string si cumple con las condiciones y lo normaliza a lower
    '''
    respuesta = input("Por cuál jugador desea hacer la consulta?  ")
    
    if re.match(r'[a-zA-Z]{4,}[ ]?[a-zA-Z]?',respuesta):
        respuesta = respuesta.lower()
    else:
        print("Debe ser un poco más específico")
        
    return respuesta         
        

def validar_logros_por_jugador(lista:list):
    '''
    Recibe una lista
    Valida si el nombre ingresado tiene coincidencias con el valor de la key nombre y muestra los logros
    No devuelve nada
    '''
    respuesta = buscar_jugador()
    
    for jugador in lista:
        if re.search(respuesta, jugador['nombre'].lower()):
            print("{0} tiene los siguientes logros: {1}".format(jugador['nombre'],jugador['logros']))

            
def validar_segun_condicion(lista:list):
    '''
    Recibe una lista
    Valida si la condicion esta en la lista de la key 
    No devuelve nada
    '''
    respuesta = buscar_jugador()
    condicion = "Miembro del Salon de la Fama del Baloncesto"
    
    for jugador in lista:
        if re.search(respuesta, jugador['nombre'].lower()):
            if condicion in jugador['logros']:
                print("{0} es parte del Salon de la Fama del Baloncesto".format(jugador['nombre']))
            else:
                print("{0} NO parte del Salon de la Fama del Baloncesto".format(jugador['nombre']))



def validar_mayor_por_valor(lista:list,key:str)->int:
    '''
    Recibe una lista y una key
    Pide al usuario dato, lo valida y muestra los valores de la key mayores al dato ingresado 
    No retorna nada
    '''

    valor_correcto = False
    
    while valor_correcto == False:
        respuesta_txt = input("Ingrese el valor deseado: ")
        
        if re.match('^[0-9]+$',respuesta_txt):
            respuesta = float(respuesta_txt)
        
            for jugador in lista:
                if jugador['estadisticas'][key] > respuesta:
                    print("{0} con un promedio de : {1}".format(jugador['nombre'],jugador['estadisticas'][key]))
                    valor_correcto = True
                
            if valor_correcto == False:
                print("No hay jugadores con promedios mayores al valor indicado")
                break
        else:
            print("Ingrese un valor numérico.")

                
def validar_mayor_por_porcentaje(lista:list,key:str)->int:
    '''
    Recibe una lista y una key
    Pide al usuario dato, lo valida y muestra los valores de la key mayores al dato ingresado
    No retorna nada
    '''
    valor_correcto = False
    
    while valor_correcto == False:
        respuesta_txt = input("Ingrese el valor deseado: ")
        
        if re.match('^[0-9]+[.]*[0-9]*$',respuesta_txt):
            respuesta = float(respuesta_txt)
        
            for jugador in lista:
                if jugador['estadisticas'][key] > respuesta:
                    print("{0} con un promedio de : {1}".format(jugador['nombre'],jugador['estadisticas'][key]))
                    valor_correcto = True
            
            if valor_correcto == False:
                print("No hay jugadores con promedios mayores al valor indicado")
                break
        else:
            print("Ingrese un porcentaje.")  


def ordenar_mostrar_mayor_porcentaje(lista:list,key:str)->int:
    '''
    Recibe por parámetro una lista y una key
    Ordena la lista por nombre posicion y muestra el porcentaje mayor al input del usuario sobre una key
    Retorna -1 si la lista está vacía y 1 si se pudo realizar el calculo
    '''
    if len(lista)>= 1:
        contador = 1
        swap = True
        
        while swap == True:
            swap = False
            for i in range(len(lista)-contador):
                
                if lista[i]['posicion'] > lista[i+1]['posicion']:
                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = auxiliar
                    swap = True         
            contador = contador + 1

        validar_mayor_por_porcentaje(lista,key)
        return 1
    else:    
        return -1

    
                
                