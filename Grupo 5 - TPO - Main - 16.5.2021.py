import jugadas
import random

def validarJugador():
    nombre=input("Jugador: ")
    while nombre.isalnum() != True:
            print("Debe ingresar un nombre con letras y/o números.")
            nombre=input("Jugador: ")
    return nombre

def imprimirPuntos():
    puntosj1,puntosj2=compDiccionario()
    print("-----------------Puntos Jugador 1: ")
    for clave in puntosj1:
        print(clave,"-",puntosj1[clave])
    print("-----------------Puntos Jugador 2: ")
    for clave in puntosj2:
        print(clave,"-",puntosj2[clave])
        
def tirar_dados(cantidad):
    dados=[]
    for i in range(int(cantidad)):
        dados.append(random.randint(1,6))
    return dados

def validar_jugada(listajugada, diccionario):
    opciones = []
    uno = jugadas.contarunos(listajugada)
    dos = jugadas.contardos(listajugada)
    tres = jugadas.contartres(listajugada)
    cuatro = jugadas.contarcuatros(listajugada)
    cinco = jugadas.contarcincos(listajugada)
    seis = jugadas.contarseises(listajugada)
    escalera = jugadas.escalera(listajugada)
    full = jugadas.fullhouse(listajugada)
    poker = jugadas.poker(listajugada)
    generala = jugadas.generala(listajugada)
    if diccionario["Uno"] == None:
        opciones.append(uno)
    if diccionario["Dos"] == None:
        opciones.append(dos)
    if diccionario["Tres"] == None:
        opciones.append(tres)
    if diccionario["Cuatro"] == None:
        opciones.append(cuatro)    
    if diccionario["Cinco"] == None:
        opciones.append(cinco)
    if diccionario["Seis"] == None:
        opciones.append(seis)
    if diccionario["Escalera"] == None:
        opciones.append(escalera)
    if diccionario["Full"] == None:
        opciones.append(full)
    if diccionario["Poker"] == None:
        opciones.append(poker)
    if diccionario["Generala"] == None:
        opciones.append(generala)        
    return opciones


def turno(diccionarioX): #FALTA COMO MANTENER CIERTOS DADOS DE TIRADA A TIRADA Y PONERLOS EN EL DICCIONARIO, FALTA PASAR COMO PARAMETRO EL JUGADOR
    lista_jugadas_bien = ["Uno","Dos","Tres","Cuatro", "Cinco", "Seis", "Escalera", "Full", "Poker", "Generala"]
    resultado = () # Tupla con 2 valores
    lista_dados_auxiliar = []
    seguir=True
    contador_tiros= 0
    cantidad_dados = 5  
    palabras_clave = diccionarioX.keys()
    lista_resultados_obtenidos = []

    for x in palabras_clave: 
        if (diccionarioX[x] != None):
            lista_resultados_obtenidos.append(x)
    lista_resultados_obtenidos.pop(0)

    while(int(contador_tiros) <= 3 and seguir == True):
        dados = tirar_dados(cantidad_dados)
        contador_tiros = contador_tiros + 1
        print("Tiros:", contador_tiros)
        for x in range(len(lista_dados_auxiliar)):
            dados.append(lista_dados_auxiliar[x])
        lista_dados_auxiliar.clear()
        tirada = validar_jugada(dados, diccionarioX) #AGREGAR VALIDACIÓN PARA SABER QUE DICCIONARIO ES
        print("Los dados de la tirada son los siguientes: ", dados)
        print("Los resultados posibles de la tirada son los siguientes: ",('\n'),tirada)     
        if(contador_tiros < 3):
            pregunta = input("¿Desea seguir tirando? ")
            while pregunta.capitalize() != "Si" and pregunta.capitalize() != "No":
                pregunta = input("¿Desea seguir tirando? ")
            if pregunta.capitalize() == "No":

                final_turno = input("Para finalizar su turno, indique con que resultado desea quedarse ingresando el nombre de la jugada: ")
                while(final_turno.capitalize() not in lista_jugadas_bien or final_turno.capitalize() in lista_resultados_obtenidos):
                    final_turno = input("Por favor, ingrese un parametro valido: ")

                for x in range(len(tirada)):
                    if final_turno.capitalize() in tirada[x][0]:
                        resultado = tuple(tirada[x])                        
                seguir = False
            elif pregunta.capitalize() == "Si":
                dados_guardados = 0
                pregunta2 = None
                while(pregunta2 != -1 and dados_guardados != 5):
                    pregunta2 = int(input("Indique el numero de dado que desea guardar para la proxima tirada. (Sino desea guardar mas dados ingrese -1):"))                        
                    while(pregunta2 != -1 and pregunta2 not in dados):
                        pregunta2 = int(input("Por favor ingrese un dato valido:"))
                    if (pregunta2 in dados):
                        lista_dados_auxiliar.append(pregunta2)
                        dados.remove(pregunta2)
                        dados_guardados = dados_guardados + 1 
                        print("Auxiliar:", lista_dados_auxiliar)                    
                cantidad_dados = 5 - dados_guardados
                        
        elif contador_tiros == 3: 
            
            final_turno2 = input("Esta es la tercer tirada del turno, por favor indique con que resultado desea quedarse ingresando el nombre de la jugada ")
            while(final_turno2.capitalize() not in lista_jugadas_bien or final_turno2.capitalize() in lista_resultados_obtenidos):
                    final_turno2 = input("Por favor, ingrese un parametro valido: ")
            for x in range(len(tirada)):
                if final_turno2.capitalize() in tirada[x][0]:
                    resultado = tuple(tirada[x])
            seguir = False
    return resultado # Retorno el resultado del turno

def guardar_resultado(diccionarioX):
    rfinal = turno(diccionarioX)
    clave,valor=rfinal
    diccionarioX[clave]=valor
    print()
    print("*"*40)
    print("Puntos del Jugador.")
    for clave in diccionarioX:
        print(clave,"-",diccionarioX[clave])
    
               
j1=validarJugador()
j2=validarJugador()
player1={"Nombre Jugador 1": j1,"Uno":None,"Dos":None,"Tres":None,"Cuatro":None,"Cinco":None,"Seis":None,"Escalera":None,"Full":None,"Poker":None,"Generala":None}
player2={"Nombre Jugador 2": j2,"Uno":None,"Dos":None,"Tres":None,"Cuatro":None,"Cinco":None,"Seis":None,"Escalera":None,"Full":None,"Poker":None,"Generala":None}

tur_no=1
while tur_no <=4:
    if tur_no%2==0:
        print()
        print("Turno Jugador 2".center(60))
        guardar_resultado(player2)
    else:
        print()
        print("Turno Jugador 1".center(60))
        guardar_resultado(player1)
    tur_no=tur_no+1

#print(guardar_resultado(player1,player2))