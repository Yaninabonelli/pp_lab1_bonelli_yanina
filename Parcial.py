from Parcial.biblioteca_archivos import*
from Parcial.biblioteca_funciones import*
from Parcial.biblioteca_calculos import*

archivo_json = "C:/Users/User/Desktop/Python/dt.json"
lista_de_jugadores = parser_json(archivo_json)
lista_jugador_estadisticas = {}
continuar = True
desbloquear_case = False

while continuar == True:
    match menu_de_opciones():
        case 1:
            mostrar_jugadores(lista_de_jugadores,"posicion","Posición")
        case 2:
            lista_jugador_estadisticas = mostrar_datos_por_indice(lista_de_jugadores)
            desbloquear_case = True
        case 3:
            if desbloquear_case == True:
                generar_csv("C:/Users/User/Desktop/Python/dt.csv",lista_jugador_estadisticas)
                print("Ya generaste el archivo, encuentralo en Desktop")
            else:
                print("Antes debe ingresar a la opción 2.")
        case 4:
            validar_logros_por_jugador(lista_de_jugadores)
        case 5:
            ordenar_y_mostrar_promedio(lista_de_jugadores,'promedio_puntos_por_partido')
        case 6:
            validar_segun_condicion(lista_de_jugadores)
        case 7:
            calcular_mayor_por_key(lista_de_jugadores,"rebotes_totales",)
        case 8:
            calcular_mayor_por_key(lista_de_jugadores,"porcentaje_tiros_de_campo",)
        case 9:
            calcular_mayor_por_key(lista_de_jugadores,"asistencias_totales",)
        case 10:
            validar_mayor_por_valor(lista_de_jugadores,"promedio_puntos_por_partido")
        case 11:
            validar_mayor_por_valor(lista_de_jugadores,"promedio_rebotes_por_partido")
        case 12:
            validar_mayor_por_valor(lista_de_jugadores,"promedio_asistencias_por_partido")
        case 13:
            calcular_mayor_por_key(lista_de_jugadores,"robos_totales",)
        case 14:
            calcular_mayor_por_key(lista_de_jugadores,"bloqueos_totales",)
        case 15:
            validar_mayor_por_porcentaje(lista_de_jugadores,"porcentaje_tiros_libres")
        case 16:
            mostrar_promedio_excluyendo_menor(lista_de_jugadores,"promedio_puntos_por_partido")
        case 17:
            pass
        case 18:
            validar_mayor_por_porcentaje(lista_de_jugadores,"porcentaje_tiros_triples")
        case 19:
            calcular_mayor_por_key(lista_de_jugadores,"temporadas",)
        case 20:
            ordenar_mostrar_mayor_porcentaje(lista_de_jugadores,"porcentaje_tiros_de_campo")
        case 21:
            pass
        case 22:
            print("Saliste del programa.")
            continuar = False







