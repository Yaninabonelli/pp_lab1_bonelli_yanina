import json

def parser_json(file:str)->list:
    '''
    Recibe como parámetro un archivo json
    Lee el archivo y lo convierte e una lista
    Devuelve una lista
    '''
    diccionario = {}
    lista = []
    with open(file,"r") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario['jugadores']
    return lista



def generar_csv(file:str, lista:list):
    '''
    Recibe como parametro una lista y la ruta de donde se va a crear un nuevo file
    Convierte la lista a formato CSV
    No devuelve nada
    '''
    with open (file,"w") as archivo:   
        for jugador in lista:
            linea_texto = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(jugador['nombre'],
                                                                                jugador['estadisticas']['temporadas'],
                                                                                jugador['estadisticas']['puntos_totales'],
                                                                                jugador['estadisticas']['promedio_puntos_por_partido'],
                                                                                jugador['estadisticas']['rebotes_totales'],                                                        
                                                                                jugador['estadisticas']['promedio_rebotes_por_partido'],
                                                                                jugador['estadisticas']['asistencias_totales'],
                                                                                jugador['estadisticas']['promedio_asistencias_por_partido'],
                                                                                jugador['estadisticas']['robos_totales'],
                                                                                jugador['estadisticas']['bloqueos_totales'],
                                                                                jugador['estadisticas']['porcentaje_tiros_de_campo'],
                                                                                jugador['estadisticas']['porcentaje_tiros_libres'],
                                                                                jugador['estadisticas']['porcentaje_tiros_triples']) 
            archivo.write(linea_texto)
            
            