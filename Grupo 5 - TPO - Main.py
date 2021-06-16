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
    if diccionario["Uno"] == "":
        opciones.append(uno)
    if diccionario["Dos"] == "":
        opciones.append(dos)
    if diccionario["Tres"] == "":
        opciones.append(tres)
    if diccionario["Cuatro"] == "":
        opciones.append(cuatro)    
    if diccionario["Cinco"] == "":
        opciones.append(cinco)
    if diccionario["Seis"] == "":
        opciones.append(seis)
    if diccionario["Escalera"] == "":
        opciones.append(escalera)
    if diccionario["Full"] == "":
        opciones.append(full)
    if diccionario["Poker"] == "":
        opciones.append(poker)
    if diccionario["Generala"] == "":
        opciones.append(generala)        
    return opciones


def turno(): #FALTA COMO MANTENER CIERTOS DADOS DE TIRADA A TIRADA Y PONERLOS EN EL DICCIONARIO, FALTA PASAR COMO PARAMETRO EL JUGADOR
    lista_jugadas_bien = ["Uno","Dos","Tres","Cuatro", "Cinco", "Seis", "Escalera", "Full", "Poker", "Generala"]
    resultado = () # Tupla con 2 valores
    lista_dados_auxiliar = []
    seguir=True
    contador_tiros= 0
    cantidad_dados = 5  
    while(int(contador_tiros) <= 3 and seguir == True):
        dados = tirar_dados(cantidad_dados)
        contador_tiros = contador_tiros + 1
        print("Tiros:", contador_tiros)
        for x in range(len(lista_dados_auxiliar)):
            dados.append(lista_dados_auxiliar[x])
        tirada = validar_jugada(dados, player1) #AGREGAR VALIDACIÓN PARA SABER QUE DICCIONARIO ES
        print("Los dados de la tirada son los siguientes: ", dados)
        print("Los resultados posibles de la tirada son los siguientes: ",('\n'),tirada)     
        if(contador_tiros < 3):
            pregunta = input("¿Desea seguir tirando? ")
            while pregunta.capitalize() != "Si" and pregunta.capitalize() != "No":
                pregunta = input("¿Desea seguir tirando? ")
            if pregunta.capitalize() == "No":

                final_turno = input("Para finalizar su turno, indique con que resultado desea quedarse ingresando el nombre de la jugada: ")
                while(final_turno not in lista_jugadas_bien):
                    final_turno = input("Por favor, ingrese un parametro valido: ")

                for x in range(len(tirada)):
                    if final_turno.capitalize() in tirada[x][0]:
                        resultado = tuple(tirada[x])                        
                seguir = False
            elif pregunta.capitalize() == "Si": 
                pregunta2 = int(input("Indique el numero de dado que desea guardar para la proxima tirada. (Sino desea guardar mas dados ingrese -1): "))
                while(pregunta2 != -1 and cantidad_dados > 1 and pregunta2 not in dados):
                    pregunta2 = int(input("Por favor ingrese un dato valido:"))
                if (pregunta2 in dados):
                    lista_dados_auxiliar.append(pregunta2)
                    dados.remove(dados[pregunta2])
                    cantidad_dados = cantidad_dados -1
                    print("Auxiliar:", lista_dados_auxiliar)


                    #verificamos que este en la lista, si no esta repreguntamos y si esta
                    # sacamos el dado lista 
                    # ¿Algun otro numero? 
                    # verificamos que este en la lista, si no esta repreguntamos y si esta
                    # sacamos el dado lista  
                    # Hasta 4
        elif contador_tiros == 3: 
            
            final_turno2 = input("Esta es la tercer tirada del turno, por favor indique con que resultado desea quedarse ingresando el nombre de la jugada ")
            while(final_turno2 not in lista_jugadas_bien):
                    final_turno2 = input("Por favor, ingrese un parametro valido: ")
            for x in range(len(tirada)):
                if final_turno2.capitalize() in tirada[x][0]:
                    resultado = tuple(tirada[x])
            seguir = False
    return resultado # Retorno el resultado del turno

def contador_Turnos(diccionario1,diccionario2):
    turnos = 1
    rfinal = turno()
    if turnos % 2 == 0:
        clave,valor=rfinal
        diccionario2[clave]=valor
    else:
        clave,valor=rfinal
        diccionario1[clave]=valor
    return diccionario1,diccionario2


j1=validarJugador()
j2=validarJugador()
player1={"Nombre": j1,"Uno":"1","Dos":"","Tres":"","Cuatro":"","Cinco":"","Seis":"","Escalera":"","Full":"","Poker":"","Generala":""}
player2={"Nombre": j2,"Uno":"","Dos":"","Tres":"","Cuatro":"","Cinco":"","Seis":"","Escalera":"","Full":"","Poker":"","Generala":""}

print(contador_Turnos(player1,player2))