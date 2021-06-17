player1={"Nombre Jugador 1": "J1","Uno": 1,"Dos": 2,"Tres":None,"Cuatro":None,"Cinco":None,"Seis":None,"Escalera":None,"Full":None,"Poker":None,"Generala":None}
mostrar = player1.keys()
lista_resultados_obtenidos = []

for x in mostrar: 
    if (player1[x] != None):
        lista_resultados_obtenidos.append(x)
lista_resultados_obtenidos.pop(0)
print("Lista que quiero: ", lista_resultados_obtenidos)