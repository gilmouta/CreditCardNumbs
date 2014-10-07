import random

def conv_to_int(y):
	"""Esta função converte uma dada string 'y' de integers para uma array de integers."""
	p = []
	for i in range(len(y)): 
		n = int(y[i])
		p.append(n)
	return p
	
def mul_sub(p):
	"""Esta função multiplica todos os integers em indexes impares por 2 e depois subtrai 9 de todos com valor maior que 9."""
	j = 0
	while j < len(p):
		if j % 2 == 0: #Multiplico os integers nos indexes ímpares por 2
			p[j] = p[j] * 2
			if p[j] > 9: #Se um integer for maior do que 9, subtraio 9 desse integer
				p[j] = p[j] - 9
		j = j + 1
	return p

def calc_soma(y):
	"""A função pega numa array de integers e adiciona-os todos uns aos outros ((k) + (k+1) + (k+2)...)"""
	p = mul_sub(conv_to_int(y))
	soma = 0
	for k in p: #Encontrar a soma de todos os números da array
		soma += k	
	print (soma)
	return soma

def luhn_verifica(x):
	"""Verifica se o dado número funciona com o método Luhn. A função faz o seguinte:
		
		- retira o último digito de (x)
		- inverte o número (x)
		- multiplica os integers que se encontram em indexes impares por 2 e subtrai 9 de todos os digitos maiores que 9
		- calcula a soma de todos os digitos do número (x)
		- verifica se a soma é divisivél por 10 (sem restos), se sim então é compativél com o método Luhn, se não não é"""
	y = str(x)
	z = str(x)
	p = []
	j = 0
	soma = 0
	
	#Vamos usar o slicing operator do python (':') para 'brincar' com as strings
	
	#Tirar o último caracter
	y = y[:-1]  #[:] vai buscar todos os characters na string excepto [-1] que é o último número
	
	#Inverter o número
	y = y[::-1]
		
	conv_to_int(z)
	mul_sub(p)
	soma = calc_soma(z)
	
	if soma % 10 == 0: #Se for divisivel por 10 então o número funciona de acordo com Luhn
		return True
	else:
		return False	
	
def length_check(x):
	'''Verifica se o tamanho do numero inserido (x), é igual a um dos tamanhos possiveis'''
	y = str(x)
	poss_leng = [13, 14, 15, 16, 19] #Os tamanhos possiveis
	resultado1 = False
	i = 0
	
	while i < len(poss_leng): #Compara o tamanho do input com os tamanhos possíveis
		if len(y) == poss_leng[i]:
			resultado1 = True
			break
		i += 1
		
	if resultado1 == True:
		return True
	else:
		return False

def digito_verificacao(x):
	"""TO DO: Fazer este comentario"""
	y = eval(x)#Funcao recebe string, converte em inteiro para poder fazer operacoes
	soma = calc_soma(x)
	if soma%10 == 0:
		digito = "0" # Se o ultimo digito for 0, devolve "0"
	else:
		digito = str(10-(soma % 10)) # Se nao, calcula fazendo 10 - ultimo digito
	return digito
        
        
def gera_num_cc(rede):
	"""TO DO: Fazer este comentario"""
	# Da para simplificar com codigo ja feito?
	if rede == "AE":
		prefixo = random.choice(["34", "37"])
		length = 15
	elif rede == "DCI":
		prefixo = random.choice(["309", "36", "38", "39"])
		length = 14    
	elif rede == "DC":
		prefixo = "65"
		length = 16    
	elif rede == "M":
		prefixo = random.choice(["5018", "5020", "5038"])
		length = random.choice([13, 19])
	elif rede == "MC":
		prefixo = random.choice(["50", "51", "52", "53", "54", "19"])
		length = 16 
	elif rede == "VE":
		prefixo = random.choice(["4026", "426", "4405", "4508"])
		length = 16    
	elif rede == "V":
		prefixo = random.choice(["4024", "4532", "4556"])
		length = random.choice([13, 16])   
	else: 
		print ("Cartao invalido")
		return False # O que por aqui? Break n parece funcionar

	nmeio= ""
	while len(nmeio) != lenght-len(prefixo)-1:  # Enquanto houverem menos numeros que os necessarios -1 (para n de verificacao)
		nmeio = nmeio + str(random.randint(0, 9))  # Ir adicionando numeros de 0 a 9

	nfim = digito_verificacao(prefixo+nmeio)  # Adicionar numero de verificacao

	numerocc(prefixo+nmeio+nfim) #Ainda nao funciona, falta numerocc

	print (numerocc)  # Print de um numero valido. Fazer return?

#Temporário, esta linha vai ser removida, está aqui só para os testes serem mais rápidos.	
print (luhn_verifica(4556737586899855))
print (length_check(4556737586899855))
