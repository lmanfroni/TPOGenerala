def generala(listajugada):
    checkgen = 0
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) > 4:
            checkgen = 1
        break
    return checkgen

def poker(listajugada):
    check = 0
    for x in range(len(listajugada)):
        if listajugada.count(listajugada[x]) > 3:
            check = 1
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
        checkfull = 1
    return checkfull

def escalera(listajugada):
    listajugada.sort()
    checkescalera = 0
    if listajugada == [1,2,3,4,5] or listajugada == [2,3,4,5,6] or listajugada == [1,3,4,5,6]:
        checkescalera = 1
    return checkescalera

def contarseises(listajugada):
    seises = listajugada.count(6)
    return seises

def contarcincos(listajugada):
    cincos = listajugada.count(5)
    return cincos

def contarcuatros(listajugada):
    cuatros = listajugada.count(4)
    return cuatros

def contartres(listajugada):
    tres = listajugada.count(3)
    return tres

def contardos(listajugada):
    dos = listajugada.count(2)
    return dos

def contarunos(listajugada):
    unos = listajugada.count(1)
    return unos

#test 123
