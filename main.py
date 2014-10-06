def conv_to_int(y):
	p = []
	for i in range(len(y)): 
		n = int(y[i])
		p.append(n)
	return p
	
def mul_sub(p):
	j = 0
	while j < len(p):
		if j % 2 == 0: #Multiplico os integers nos indexes ímpares por 2
			p[j] = p[j] * 2
			if p[j] > 9: #Se um integer for maior do que 9, subtraio 9 desse integer
				p[j] = p[j] - 9
		j = j + 1
	return p

def calc_soma(y):
	p = mul_sub(conv_to_int(y))
	soma = 0
	for k in p: #Encontrar a soma de todos os números da array
		soma += k	
	soma = soma
	print (soma)
	return soma

def luhn_verifica(x):
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
	
	
#Temporário, esta linha vai ser removida, está aqui só para os testes serem mais rápidos.	
print (luhn_verifica(4556737586899855))
print (length_check(4556737586899855))
