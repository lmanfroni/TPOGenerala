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
    if listajugada.count(6) = 5:
        seises = ("Seis", 30)
    elif listajugada.count(6) = 4:
        seises = ("Seis", 24)
    elif listajugada.count(6) = 3:
        seises = ("Seis", 18)
    elif listajugada.count(6) = 2:
        seises = ("Seis", 12)
    elif listajugada.count(6) = 1:
        seises = ("Seis", 6)
    elif listajugada.count(6) = 0:
        seises = ("Seis", 0)
    return seises

def contarcincos(listajugada):
    if listajugada.count(5) = 5:
        cincos = ("Cinco", 25)
    elif listajugada.count(5) = 4:
        cincos = ("Cinco", 20)
    elif listajugada.count(5) = 3:
        cincos = ("Cinco", 15)
    elif listajugada.count(5) = 2:
        cincos = ("Cinco", 10)
    elif listajugada.count(5) = 1:
        cincos = ("Cinco", 5)
    elif listajugada.count(5) = 0:
        cincos = ("Cinco", 0)
    return cincos

def contarcuatros(listajugada):
    if listajugada.count(4) = 5:
        cuatros = ("Cuatro", 20)
    elif listajugada.count(4) = 4:
        cuatros = ("Cuatro", 16)
    elif listajugada.count(4) = 3:
        cuatros = ("Cuatro", 12)
    elif listajugada.count(4) = 2:
        cuatros = ("Cuatro", 8)
    elif listajugada.count(4) = 1:
        cuatros = ("Cuatro", 4)
    elif listajugada.count(4) = 0:
        cuatros = ("Cuatro", 0)
    return cuatros

def contartres(listajugada):
    if listajugada.count(3) = 5:
        tres = ("Tres", 15)
    elif listajugada.count(3) = 4:
        tres = ("Tres", 12)
    elif listajugada.count(3) = 3:
        tres = ("Tres", 9)
    elif listajugada.count(3) = 2:
        tres = ("Tres", 6)
    elif listajugada.count(3) = 1:
        tres = ("Tres", 3)
    elif listajugada.count(3) = 0:
        tres = ("Tres", 0)
    return tres

def contardos(listajugada):
    if listajugada.count(2) = 5:
        dos = ("Dos", 10)
    elif listajugada.count(2) = 4:
        dos = ("Dos", 8)
    elif listajugada.count(2) = 3:
        dos = ("Dos", 6)
    elif listajugada.count(2) = 2:
        dos = ("Dos", 4)
    elif listajugada.count(2) = 1:
        dos = ("Dos", 2)
    elif listajugada.count(2) = 0:
        dos = ("Dos", 0)
    return dos

def contarunos(listajugada):
    unos = listajugada.count(1)
    return unos
