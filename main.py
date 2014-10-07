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
	soma = 0
	z = y[-1]

	#y = y[:-1]  #[:] vai buscar todos os characters na string excepto [-1] que é o último número
	y = y[:-1] #Remover o último caracter
	print(y)
	y = y[::-1] #Inverter o input
	print(y)
	y = mul_sub(conv_to_int(y))
	print(y)
	for k in y: #Encontrar a soma de todos os números da array
		soma += int(k)
	return soma + eval(z)

def luhn_verifica(x):
	"""Verifica se o dado número funciona com o método Luhn. A função faz o seguinte:
		
		- retira o último digito de (x)
		- inverte o número (x)
		- multiplica os integers que se encontram em indexes impares por 2 e subtrai 9 de todos os digitos maiores que 9
		- calcula a soma de todos os digitos do número (x)
		- verifica se a soma é divisivél por 10 (sem restos), se sim então é compativél com o método Luhn, se não não é"""
	s = str(x)
	y = str(x)
	soma = 0
	
	soma = calc_soma(y) + eval(s[-1])	
	print (soma)
	
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

def prefix_check(x):
	y = str(x)
	prefix = ["34", "37", "309" , "36", "38", "39", "65", "5018", "5020", "5038", "50", "51", "52", "53", "54", "19", "4026", "426", "4405", "4508", "4024", "4532", "4556"]
	i = 0
	resultado = False
	while i < len(prefix):
		if y[len(prefix[i])] == prefix[i]:
			resultado = True
			return resultado
		i += 1

def digito_verificacao(x):
	"""TO DO: Fazer este comentario"""
	#y = eval(x)#Funcao recebe string, converte em inteiro para poder fazer operacoes
	s = str(x)
	
	soma = calc_soma(s)
	print (soma)
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

	nmeio= ""
	while len(nmeio) != length-len(prefixo)-1:  # Enquanto houverem menos numeros que os necessarios -1 (para n de verificacao)
		nmeio = nmeio + str(random.randint(0, 9))  # Ir adicionando numeros de 0 a 9
	nfim = digito_verificacao(prefixo+nmeio)  # Adicionar numero de verificacao
	numerocc = prefixo+nmeio+nfim
	
	print (numerocc)  # Print de um numero valido. Fazer return?

	return numerocc

#Temporário, estas linhas vai ser removida, está aqui só para os testes serem mais rápidos.
x = gera_num_cc("AE")
#x = 4556245018079	
print (luhn_verifica(x))
print ("------------------------------------")
print (digito_verificacao(x))
print ("------------------------------------")
print (x)
print (calc_soma("3248"))
