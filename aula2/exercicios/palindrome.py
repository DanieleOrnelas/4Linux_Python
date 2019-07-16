#!/usr/bin/python3

#Programa para verificar se uma palavra digitada é palindrome (mesma escrita de tras para frente)
palavra = input('Digite a palavra: ')
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
	print('A palavra ' + palavra + ' é uma palindrome')
else:
	print('A palavra ' + palavra + ' não é uma palindrome')