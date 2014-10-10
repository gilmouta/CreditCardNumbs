import random

listarede = [  #RedeIniciais: Length, Prefixo, Nome Rede
        ["AE", [15], ["34", "37"], "American Express"],
        ["DCI", [14], ["309", "36", "38", "39"], "Diners Club International"],     #Para chamar: listarede["INICIAL"][x]
        ["DC", [16], ["65"], "Discover Card"],                                     # 0 = abreviatura     1 = length    2 = prefixo       3 = nome da rede
        ["M", [13,19], ["5018", "5020", "5038"], "Maestro"],      
        ["MC", [16], ["50", "51", "52", "53", "54", "19"], "Master Card"],
        ["VE", [16], ["4026", "426", "4405", "4508"], "Visa Electron"],
        ["V", [13, 16], ["4024", "4532", "4556"], "Visa"]]

def calc_soma(x):
	""" Recebe string, devolve integer"""
	i = 0
	soma = 0
	x = x[::-1]   #Inverter o input

	while i < len(x):  #Enquanto nao tivermos chegado ao ultimo numero
		num = eval(x[i])  #Transforma o numero em que estamos num inteiro
		if i % 2:
			soma = soma + num #Se esse numero estiver num index par, soma-se a soma
		else: #Se estiver num index impar, multiplica-se por 2 primeiro
			num = num*2
			if num > 9: #Se o resultado for maior que 9, tira-se 9
				num = num - 9
			soma = soma + num
		i += 1
	return soma

def luhn_verifica(x):
	"""Verifica se o dado número funciona com o método Luhn. A função faz o seguinte:
		
		- retira o último digito de (x)
		- inverte o número (x)
		- multiplica os integers que se encontram em indexes impares por 2 e subtrai 9 de todos os digitos maiores que 9
		- calcula a soma de todos os digitos do número (x)
		- verifica se a soma é divisivél por 10 (sem restos), se sim então é compativél com o método Luhn, se não não é"""
	s = str(x)
	soma = 0
	
	soma = calc_soma(s[0:-1]) + eval(s[-1])	
	
	if soma % 10 == 0: #Se for divisivel por 10 então o número funciona de acordo com Luhn
		return True
	else:
		return False	


def prefix_check(x):
	y = str(x)
	i = 0
	j = 0
	res = False
	while i < len(listarede):
		while j < len(listarede[i][2]):
			if comeca_por_um(y, listarede[i][2]):
				res = True
				break
			else:
				j += 1			
		j = 0
		i +=1
	return res
	
		
def comeca_por(cad1, cad2):
	if cad1[0:len(cad2)] == cad2:
		return True
	else:
		return False	
	
def comeca_por_um(cad, t_cads):
	i = 0
	res = False
	while i < len(t_cads):
		if comeca_por(cad, t_cads[i]) == True:
			res = True
			return res
		else:
			i += 1
	return res


def valida_iin(x):
	x = str(x)
	i = 0
	j = 0
	while not(comeca_por_um(x, listarede[i][2])):
		i = i+1
		j = i
		if j == len(listarede):
			return ""
	return listarede[j][3]		
		
def digito_verificacao(x):
	"""TO DO: Fazer este comentario"""
	#y = eval(x)#Funcao recebe string, converte em inteiro para poder fazer operacoes
	s = str(x)
	
	soma = calc_soma(s)
	if soma%10 == 0:
		digito = "0" # Se o ultimo digito for 0, devolve "0"
	else:
		digito = str(10-(soma % 10)) # Se nao, calcula fazendo 10 - ultimo digito
	return digito
       
def gera_num_cc(rede):
	"""TO DO: Fazer este comentario"""
	i = 0
	j = -1
	while i < len(listarede):
		if listarede[i][0] == rede:  #Se a rede está na lista de redes
			j = i   #j = indice abreviatura

		i += 1
	if j == -1:  #Se rede for invalida (nao encontrou abreviatura
		print("Rede invalida")			
		return False

	length = random.choice(listarede[j][1])
	prefixo = random.choice(listarede[j][2])

	nmeio= ""
	while len(nmeio) != length-len(prefixo)-1:  # Enquanto houverem menos numeros que os necessarios -1 (para n de verificacao)
		nmeio = nmeio + str(random.randint(0, 9))  # Ir adicionando numeros de 0 a 9
	nfim = digito_verificacao(prefixo+nmeio)  # Adicionar numero de verificacao
	numerocc = prefixo+nmeio+nfim

	return numerocc


#Temporário, estas linhas vai ser removida, está aqui só para os testes serem mais rápidos.
#x = gera_num_cc("FUCK")
x = gera_num_cc(random.choice(["AE", "DCI", "DC", "M", "MC", "VE", "V"]))
print ("Numero Cartao: ", x)
print ("------------------------------------")
#print ("Verifica Luhn? ", luhn_verifica(x))
#print ("Verifica tamanho? ", length_check(x))
print ("Verifica prefixo? ", prefix_check(x))
#x = "012345"
#y = ("22", "012345", "023")
#print(comeca_por_um(x,y))

#comeca_por("3", listarede[0][2][0])

print(valida_iin(x))
