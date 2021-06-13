def generala(listajugada):
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) == 5:
            checkgen = ("Generala", 50)
        else: 
			checkgen = ("Generala", 0)		
    return checkgen

def poker(listajugada):
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) == 4:
            check = ("Poker", 40)
        else: 
			check = ("Poker", 0)
    return check

def fullhouse(listajugada):
    trio = 0
    duo = 0
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) == 2:
            duo = 1
        elif listajugada.count(listajugada[x]) == 3:
            trio = 1
    if trio == 1 and duo == 1:
        checkfull = ("Full", 30)
    else: 
		checkfull = ("Full", 0)
    return checkfull

def escalera(listajugada):
    listajugada.sort()
    if listajugada == [1,2,3,4,5] or listajugada == [2,3,4,5,6] or listajugada == [1,3,4,5,6]:
        checkescalera = ("Escalera", 20)
    else:
		checkescalera = ("Escalera", 0)
    return checkescalera

def contarseises(listajugada):
    check = listajugada.count(6)
    seises = check * 6
    return seises

def contarcincos(listajugada):
    check = listajugada.count(5)
    cincos = check * 5
    return cincos

def contarcuatros(listajugada):
    check = listajugada.count(4)
    cuatros = check * 4
    return cuatros

def contartres(listajugada):
    check = listajugada.count(3)
    tres = check * 3
    return tres

def contardos(listajugada):
    check = listajugada.count(2)
    dos = check * 2
    return dos

def contarunos(listajugada):
    unos = listajugada.count(1)
    return unos
