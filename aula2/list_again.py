#!/usr/bin/python3

#MOSTRAR VALORES PARES DE UMA SEQUÊNCIA DE NÚMEROS

#AINDA USANDO LISTA
'''
#forma 1
pot = []

for valor in range(1,11):
	if valor % 2 == 0: #Se o resto da divisao por dois for igual a zero
		pot.append(valor)

#forma 2

pot = [valor for valor in range(1,11) if valor % 2 == 0]

print(pot)
'''