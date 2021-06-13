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

def validar_jugada(listajugada):
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
    opciones.extend([uno,dos,tres,cuatro,cinco,seis,escalera,full,poker,generala])

    return opciones

def turno(): #FALTA COMO MANTENER CIERTOS DADOS DE TIRADA A TIRADA Y PONERLOS EN EL DICCIONARIO, FALTA PASAR COMO PARAMETRO EL JUGADOR
    seguir=True
    contador_tiros=1
    cantidad_dados = 5
    while(int(contador_tiros) <= 3 and seguir == True):
        dados = tirar_dados(cantidad_dados)
        contador_tiros = contador_tiros + 1
        tirada = validar_jugada(dados)
        print("Los dados de la tirada son los siguientes: ", dados)
        print("Los resultados posibles de la tirada son los siguientes: ",('\n'),"Uno: ", tirada[0]," Dos: ", tirada[1]," Tres: ", tirada[2]," Cuatro: ", tirada[3]," Cinco: ", tirada[4]," Seis: ", tirada[5]," Escalera: ", tirada[6]," Full: ",tirada[7]," Poker: ",tirada[8]," Generala: ",tirada[9])     
        consulta = "Si"
        if(contador_tiros < 3):
            consulta = input("¿Desea seguir tirando? ")
            while consulta != "Si" and consulta != "No":
                consulta = input("¿Desea seguir tirando?")
        else:
            consulta = "No"
        if(consulta == "No"):
            seguir=False
    return
               
j1=validarJugador()
j2=validarJugador()
player1={"Nombre": j1,"Uno ":"","Dos ":"","Tres ":"","Cuatro":"","Cinco":"","Seis":"","Escalera":"","Full":"","Poker":"","Generala":""}
player2={"Nombre": j2,"Uno ":"","Dos ":"","Tres ":"","Cuatro":"","Cinco":"","Seis":"","Escalera":"","Full":"","Poker":"","Generala":""}

turno()
