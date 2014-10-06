#Vamos usar o slicing operator do python (':') para 'brincar' com as strings

def luhn_verifica(x):
	y = str(x)
	z = str(x)
	p = []
	i = 0
	j = 0
	k = 0
	soma = 0
	
	#Tirar o último carácter
	y = y[:-1]  #[:] vai buscar todos os characters na string excepto [-1] que é o último número
	
	#Inverter o número
	y = y[::-1]
	
	for i in range(len(y)):
		n = int(y[i])
		p.append(n)
	
	while j < len(p):
		if j % 2 == 0:
			p[j] = p[j] * 2
			if p[j] > 9:
				p[j] = p[j] - 9
		j = j + 1
		
	for k in p:
		soma += k	
	soma = soma + eval(z[-1])
	
	if soma % 10 == 0:
		print("Coolio")
	else:
		print("...what")
	
	
#Temporário, esta linha vai ser removida, está aqui só para os testes serem mais rápidos.	
luhn_verifica(4556737586899855)
