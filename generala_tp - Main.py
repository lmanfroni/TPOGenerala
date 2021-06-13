import random

def tirar_dados(cantidad=5):
    dados=[]
    for i in range(int(cantidad)):
        dados.append(random.randint(1,6))
    return dados

def turno():
	seguir=True
	contador_tiros=1
	mensaje = "Listo"
	while(int(contador_tiros) <= 3 and seguir == True):
		dados = tirar_dados()
		# ~ validacion = validar_todo(dados)	
		contador_tiros = contador_tiros + 1
		print(dados)
		if(contador_tiros < 3):
			consulta = input("¿Desea seguir tirando?")
		if(consulta == "No"):
			seguir=False
	return mensaje			


print(turno())				
		
