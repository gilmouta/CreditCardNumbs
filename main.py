#81976 - Marco Coelho / 82003 - Gil Mouta / 82078, Guilherme Serpa / Grupo 54

import random

listarede = [  	 #Iniciais Rede, Length, Prefixo, Nome Rede
        ["AE", [15], ["34", "37"], "American Express"],
        ["DCI", [14], ["309", "36", "38", "39"], "Diners Club International"],  
        ["DC", [16], ["65"], "Discover Card"],                               
        ["M", [13,19], ["5018", "5020", "5038"], "Maestro"],      
        ["MC", [16], ["50", "51", "52", "53", "54", "19"], "Master Card"],
        ["VE", [16], ["4026", "426", "4405", "4508"], "Visa Electron"],
        ["V", [13, 16], ["4024", "4532", "4556"], "Visa"]]

listacategoria = ["Companhias aereas", 
                  "Companhias aereas e outras tarefas futuras da industria",
                  "Viagens e entretenimento e bancario / financeiro",
                  "Servicos bancarios e financeiros", 
                  "Servicos bancarios e financeiros", 
                  "Merchandising e bancario / financeiro", 
                  "Petroleo e outras atribuicoes futuras da industria",
                  "Saude, telecomunicacoes e outras atribuicoes futuras da industria", 
                  "Atribuicao nacional"]

def calc_soma(x):
	'''
	String --> Int
	
	Inverte o numero, multiplica os digitos na posicao impar por 2 e subtrai 9 
	a todos os digitos maiores do que 9. De seguida adiciona todos os digitos. '''
	i, soma = 0, 0
	x = x[::-1]

	while i < len(x):
		num = eval(x[i])	
		if i % 2:
			soma = soma + num 
		else: 
			num = num*2						
			if num > 9: 	
				num = num - 9
			soma = soma + num
		i += 1
	return soma

def luhn_verifica(x):
	'''
	Int/String --> Boolean
	
	Devolve True se o dado numero verifica o algoritmo de Luhn.'''
	
	s = str(x)
	soma = calc_soma(s[0:-1]) + eval(s[-1])				
	return soma % 10 == 0 		
		
def comeca_por(cad1, cad2):
	'''
	String --> Boolean
	
	Devolve True se o primeiro argumento comecar pelo segundo argumento.'''
	return cad1[0:len(cad2)] == cad2
	
def comeca_por_um(cad, t_cads):
	'''
	String --> Boolean
	
	Devolve True se o primeiro argumento comecar por pelo menos uma string 
	do segundo argumento.'''
	i = 0
	while i < len(t_cads): 
		if comeca_por(cad, t_cads[i]) == True:
			return True
		else:
			i += 1
	return False

def valida_iin(x):
	'''
	String --> String

	Devolve o nome da rede correspondente ao numero de cartao se o tamanho 
	estiver certo e comecar por um prefixo valido. Caso contrario devolve "".'''
	x = str(x)
	i, j = 0, 0
	while not(comeca_por_um(x, listarede[i][2])): 
		i += 1 
		j = i
		if j == len(listarede):
			return ""
	if not(len(x) in listarede[j][1]):
		return ""
	return listarede[j][3] 

def categoria(x):
	'''
	String --> String
	
	Devolve a categoria do emissor correspondente ao numero de cartao.'''
	x = str(x)
	y = eval(x[0]) 
	return listacategoria[y-1]

def verifica_cc(x):
	'''
	Integer --> String[]
	
	Devolve a categoria da rede emissora e o nome da rede emissora se o numero 
	de cartao for valido. Senao devolve "cartao invalido"'''
	x = str(x)
	if luhn_verifica(x) and valida_iin(x) != "": 
		return (categoria(x), valida_iin(x))
	else:
		return "cartao invalido"
	
	
	############################### Geracao ###############################
	
def digito_verificacao(x):
	'''
	String --> String
	
	Devolve o digito final de um numero de cartao de forma a que verifique 
	o algoritmo de Luhn.'''
	s = str(x)
	soma = calc_soma(s)
	if soma%10 == 0:
		digito = "0" 
	else:
		digito = str(10-(soma % 10))
	return digito
       
def gera_num_cc(rede):
	'''
	String --> Integer
	
	Gera um numero de cartao da rede emissora dada.'''
	i, j = 0, -1
	while i < len(listarede):
		if listarede[i][0] == rede: 
			j = i 
		i += 1
	if j == -1: 	
		return "Rede invalida"

	length = random.choice(listarede[j][1])
	prefixo = random.choice(listarede[j][2])
	nmeio= ""

	while len(nmeio) != length-len(prefixo)-1:
		nmeio = nmeio + str(random.randint(0, 9))
	nfim = digito_verificacao(prefixo+nmeio) 
	numerocc = eval(prefixo+nmeio+nfim)

	return numerocc