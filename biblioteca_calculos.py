
def calcular_mayor_por_key(lista:list,key:str)->int:
    '''
    Recibe como parametro una lista y una key
    Calcula el mayor del valor de la key
    Retorna -1 si la lista está vacía y 1 si se pudo realizar el calculo
    '''
    flag = True
    
    if len(lista) >= 1:
        for jugador in lista: 
            if flag == True or jugador['estadisticas'][key] > maximo:
                maximo  = jugador['estadisticas'][key]
                nombre = jugador['nombre']
                flag = False   
        print("{0} con un máximo de: {1}".format(nombre,maximo))
        return 1
    else:
        return -1

        
def ordenar_y_mostrar_promedio(lista:list,key:str)->int:
    '''
    Recibe por parámetro una lista y una key
    Ordena la lista por nombre y muestra los valores de la key solitada y calcula el promedio
    Retorna -1 si la lista está vacía y 1 si se pudo realizar el calculo
    '''
    if len(lista)>= 1:
        contador_promedio = 0
        contador = 1
        swap = True
        
        while swap == True:
            swap = False
            for i in range(len(lista)-contador):
                
                if lista[i]['nombre'] > lista[i+1]['nombre']:
                    auxiliar = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = auxiliar
                    swap = True         
            contador = contador + 1
            
        for jugador in lista:
            contador_promedio =  contador_promedio + jugador['estadisticas'][key]
            print("{0} - Promedio de puntos {1}".format(jugador['nombre'],jugador['estadisticas'][key]))
         
        promedio = contador_promedio/len(lista)   
        print("El promedio de puntos por partido de todo el equipo del Dream Team es {0}".format(promedio))
        return 1
    else:
        return -1   

def mostrar_promedio_excluyendo_menor(lista:list,key:str)->int:
    '''
    Recibe como parametro una lista y una key
    Calcula el menor y luego lo excluye del calculo del promedio
    Retorna -1 si la lista está vacía y 1 si se pudo realizar el calculo
    '''
    if len(lista)>= 1:
        flag = True
        contador_promedio = 0
        
        for jugador in lista: 
            if flag == True or jugador['estadisticas'][key] < minimo:
                minimo  = jugador['estadisticas'][key]
                nombre = jugador['nombre']
                flag = False

        for jugador in lista:
            if jugador['nombre'] != nombre:
                contador_promedio =  contador_promedio + jugador['estadisticas'][key]

        print("El promedio de puntos por partido excluyendo al menor es {0}".format(contador_promedio/ (len(lista)-1)))
        return 1
    else:
        return -1 
    
