#!/usr/bin/python3
#DEFININDO UMA FUNÇÃO

import sys

print(sys.argv)

for k in range(len(sys.argv)):
	print('Parametro {}: {}'.format(k,sys.argv[k]))


exit()
def descobre_dic(**kwargs):
	print(kwargs)

	for k in kwargs.keys():
		print('Chave: {}'.format(k))
		print('Valor: {}'.format(kwargs[k]))

descobre_dic(nome="servidor",ip="192.168.16.1,dominio=4Linux.com.br")
print("\n")
descobre_dic(user="joaozinho",nome="joao",sobrenoome="silva",idade="20")




exit()
def calcular_fig_geometrica(*args): # O * indica que os parâmetros comporão uma lista
	if len(args) == 1:
		print('Area do quadrado: {}'.format(args[0]**2))
	elif len(args) == 2:
		print('Area do retangulo: {}'.format(args[0]*args[1]))
	else:
		print('Volume: {}'.format(args[0]*args[1]*args[2]))

calcular_fig_geometrica(2)
calcular_fig_geometrica(2,10)
calcular_fig_geometrica(2,10,10)

exit()
def animal(tipo,nome):
	print('eu tenho um {} que se chama {}'.format(tipo,nome))

animal('cachorro','rex')

exit()
def diga_ola(n):
	print('ola ' + n)
nome = input('digite o nome: ')
diga_ola(nome)

exit()
def diga_ola(n):
	print('ola ' + n)

def pergunta():
	nome = input('digite o nome: ')
	return nome

x = pergunta()
diga_ola(x)



exit()
def diga_ola():
	print('ola')
diga_ola()
