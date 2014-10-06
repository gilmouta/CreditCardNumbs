

def luhn_verifica(x):
	y = str(x)
	z = str(x)
	p = []
	j = 0
	soma = 0
	
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
		print("Funciona")
	else:			#Vai ser substituido por um return de uma boolean mais tarde
		print("Não funciona")
	
	
#Temporário, esta linha vai ser removida, está aqui só para os testes serem mais rápidos.	
luhn_verifica(4556737586899855)
