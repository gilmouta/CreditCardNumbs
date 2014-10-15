#81976 - Marco Coelho / 82003 - Gil Mouta / 82078, Guilherme Serpa / Grupo 54

import random

listarede = [  	 #RedeIniciais: Length, Prefixo, Nome Rede
        ["AE", [15], ["34", "37"], "American Express"],
        ["DCI", [14], ["309", "36", "38", "39"], "Diners Club International"],  #Para chamar: listarede["INICIAL"][x]
        ["DC", [16], ["65"], "Discover Card"],                                  # 0 = abreviatura   1 = length  2 = prefixo  3 = nome rede
        ["M", [13,19], ["5018", "5020", "5038"], "Maestro"],      
        ["MC", [16], ["50", "51", "52", "53", "54", "19"], "Master Card"],
        ["VE", [16], ["4026", "426", "4405", "4508"], "Visa Electron"],
        ["V", [13, 16], ["4024", "4532", "4556"], "Visa"]]

listacategoria = ["Companhias aereas", "Companhias aereas e outras tarefas futuras da industria","Viagens e entretenimento e bancario / financeiro","Servicos bancarios e financeiros", "Servicos bancarios e financeiros", "Merchandising e bancario / financeiro", "Petroleo e outras atribuicoes futuras da industria","Saude, telecomunicacoes e outras atribuicoes futuras da industria", "Atribuicao nacional"]

def calc_soma(x):
	'''Recebe string, devolve integer. \n Inverte o numero, multiplica os digitos na posicao impar por 2 e subtrai 9 a todos os digitos maiores do que 9. De seguida adiciona todos os digitos '''
	i, soma = 0, 0
	x = x[::-1]			#Inverter o input

	while i < len(x):		#Enquanto nao tivermos chegado ao ultimo numero
		num = eval(x[i])	#Transforma o numero em que estamos num inteiro
		if i % 2:
			soma = soma + num 	#Se esse numero estiver num index par, soma-se a soma
		else: 					#Se estiver num index impar, multiplica-se por 2 primeiro
			num = num*2						
			if num > 9: 		#Se o resultado for maior que 9, tira-se 9
				num = num - 9
			soma = soma + num
		i += 1
	return soma

def luhn_verifica(x):
	'''Recebe integer/string, devolve boolean. \n Devolve True se o dado numero verifica o algoritmo de Luhn.'''
	s = str(x)
	soma = calc_soma(s[0:-1]) + eval(s[-1])				
	return soma % 10 == 0 		#Se for divisivel por 10 entao o numero funciona de acordo com Luhn			
		
def comeca_por(cad1, cad2):
	'''Recebe duas strings, devolve boolean. \n Devolve True se o primeiro argumento comecar pelo segundo argumento.'''
	return cad1[0:len(cad2)] == cad2
	
def comeca_por_um(cad, t_cads):
	'''Recebe string (arg1) e lista de strings (arg2), devolve boolean. \n Devolve True se o primeiro argumento comecar por pelo menos uma string do segundo argumento.'''
	i = 0
	while i < len(t_cads):  # Vai de string em string da lista
		if comeca_por(cad, t_cads[i]) == True: # Se comecar por uma delas, devolve true
			return True
		else:
			i += 1
	return False

def valida_iin(x):
	'''Recebe string, devolve string. \n Devolve o nome da rede correspondente ao numero de cartao se o tamanho estiver certo e comecar por um prefixo valido. Caso contrario devolve "".'''
	x = str(x)
	i, j = 0, 0
	while not(comeca_por_um(x, listarede[i][2])): # Enquanto nao comecar por um prefixo valido...
		i += 1 # Vai de rede em rede
		j = i
		if j == len(listarede):  # Se chegou ao fim devolve ""
			return ""
	if not(len(x) in listarede[j][1]): # Se o tamanho nao corresponde ao prefixo, devolve ""
		return ""
	return listarede[j][3] # Devolve rede emissora

def categoria(x):
	'''Recebe string, devolve string. \n Devolve a categoria do emissor correspondente ao numero de cartao.'''
	x = str(x)
	y = eval(x[0]) # Poe primeiro caracter do string x no y
	return listacategoria[y-1] # Devolve categoria correspondente a y

def verifica_cc(x):
	'''Recebe inteiro, devolve lista de strings. \n Devolve a categoria da rede emissora e o nome da rede emissora se o numero de cartao for valido. Senao devolve "numero invalido"'''
	x = str(x)
	if luhn_verifica(x) and valida_iin(x) != "": 
		return (categoria(x), valida_iin(x))
	else:
		return "cartao invalido"
	
def digito_verificacao(x):
	'''Recebe string, devolve string. \n Devolve o digito final de um numero de cartao de forma a que verifique o algoritmo de Luhn.'''
	s = str(x)
	soma = calc_soma(s)
	if soma%10 == 0:
		digito = "0"  #Se o ultimo digito for 0, devolve "0"
	else:
		digito = str(10-(soma % 10)) #Se nao, calcula fazendo 10 - ultimo digito
	return digito
       
def gera_num_cc(rede):
	'''Recebe string, devolve inteiro. \n Gera um numero de cartao da rede emissora dada.'''
	i, j = 0, -1
	while i < len(listarede):
		if listarede[i][0] == rede:  #Se a rede esta na lista de redes
			j = i #j = indice abreviatura
		i += 1
	if j == -1:  #Se rede for invalida (nao encontrou abreviatura)		
		return "Rede invalida"

	length = random.choice(listarede[j][1]) # Escolhe aleatoriamente um length dos validos
	prefixo = random.choice(listarede[j][2]) # Escolhe aleatoriamente um prefixo dos validos
	nmeio= ""

	while len(nmeio) != length-len(prefixo)-1: #Enquanto houverem menos numeros que os necessarios -1
		nmeio = nmeio + str(random.randint(0, 9)) #Ir adicionando numeros de 0 a 9
	nfim = digito_verificacao(prefixo+nmeio)  #Adicionar numero de verificacao
	numerocc = eval(prefixo+nmeio+nfim)

	return numerocc