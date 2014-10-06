"""Vamos usar o slicing operator do python (':') para 'brincar' com as strings

"""

def verifica_cc(x):
	y = str(x)
	
	#Tirar o último carácter
	y = y[:-1]  #[:] vai buscar todos os characters na string excepto [-1] que é o último número
	
	#Inverter o número
	y = y[::-1]
	
	print(x) #Testing reasons of BEFORE
	print(y) #and AFTER
	
	
verifica_cc(4556737586899855) #Temporário, esta linha vai ser removida, está aqui só para os testes serem mais rápidos.
