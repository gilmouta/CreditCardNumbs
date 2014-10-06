def calc_soma(x):
""" To do em todas: estes comentarios"""
    soma = 0
    y = eval(x) # Funcao recebe string, converte em inteiro para poder fazer operacoes
    
    # Enquanto o numero tiver mais que um digito != 0 retira o ultimo digito e adiciona-o a soma
    while y != 0: 
        soma = soma + (y%10) 
        y = y // 10

    return soma

def luhn_verifica(x):
	y = str(x)
	z = str(x)
	p = []
	j = 0
	soma = 0
	resultado = None
	
	#Vamos usar o slicing operator do python (':') para 'brincar' com as strings
	
	#Tirar o último carácter
	y = y[:-1]  #[:] vai buscar todos os characters na string excepto [-1] que é o último número
	
	#Inverter o número
	y = y[::-1]
	
	#Converto a string y para uma array de integers em p[]
	for i in range(len(y)): 
		n = int(y[i])
		p.append(n)
	
	while j < len(p):
		if j % 2 == 0: #Multiplico os integers nos indexes ímpares por 2
			p[j] = p[j] * 2
			if p[j] > 9: #Se um integer for maior do que 9, subtraio 9 desse integer
				p[j] = p[j] - 9
		j = j + 1
		
	for k in p: #Encontrar a soma de todos os números da array
		soma += k	
	soma = soma + eval(z[-1])
	
	if soma % 10 == 0: #Se for divisivel por 10 então o número funciona de acordo com Luhn
		return True
	else:			#Vai ser substituido por um return de uma boolean mais tarde
		return False
	
def length_check(x):
	y = str(x)
	poss_leng = [13, 14, 15, 16, 19]
	resultado1 = False
	i = 0
	
	while i < len(poss_leng):
		if len(y) == poss_leng[i]:
			resultado1 = True
			return resultado1
			break
		i += 1
	
	
#Temporário, esta linha vai ser removida, está aqui só para os testes serem mais rápidos.	
print (luhn_verifica(4556737586899855))
print (length_check(4556737586899855)) #Known bug, will return None if False, will fix later 
