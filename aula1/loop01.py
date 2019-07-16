#!/usr/bin/python3



#Abaixo de 200 min cobrar R$ 0.20/min
#Entre 200 e 400 - R$ 0.18
#Acima de 400 - R$ 0.15

minutos = int(input('minutos utulizados: '))

if minutos < 200:
	preco = 0.2
elif minutos <= 400:
	preco = 0.18
else:
	preco = 0.15

print('Conta: R$ {:.2f}'.format(minutos * preco))




exit()
# NOVO EXEMPLO
velocidade = int(input('informe vel.: '))
if velocidade > 110:
	multa = (velocidade - 110) * 5
	print('multa: R$  {:2f}'.format(multa))


# NOVO EXEMPLO
idade = int(input('Digite idade: '))
habilitacao = input('Possui habilitação? ')
h = False

if habilitacao.lower().strip() == 'sim':
	h = True
if idade >= 18 and h == True:
	print('Pode dirigir')
else:
	print('Não pode dirigir')
