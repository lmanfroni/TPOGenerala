def generala(listajugada):
    checkgen = 0
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) > 4:
            checkgen = 50
        break
    return checkgen

def poker(listajugada):
    check = 0
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) > 3:
            check = 40
            break
    return check

def fullhouse(listajugada):
    checkfull = 0
    trio = 0
    duo = 0
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) == 2:
            duo = 1
        elif listajugada.count(listajugada[x]) == 3:
            trio = 1
    if trio == 1 and duo == 1:
        checkfull = 30
    return checkfull

def escalera(listajugada):
    listajugada.sort()
    checkescalera = 0
    if listajugada == [1,2,3,4,5] or listajugada == [2,3,4,5,6] or listajugada == [1,3,4,5,6]:
        checkescalera = 20
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
