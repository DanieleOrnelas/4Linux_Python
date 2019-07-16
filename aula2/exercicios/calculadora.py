#!/usr/bin/python3

# Calculadora simples (+,-,*,/), que recebe a entrada pelo input

def soma(num1,num2):
	return num1 + num2
def sub(num1,num2):
	return num1 - num2
def mult(num1,num2):
	return num1 * num2
def div(num1,num2):
	return num1 / num2

operacao = input('Entre com a operacao: ')
operadores ='+-*/'

for k in operacao:
	if k in operadores:
		tipo = k

# achando os numeros
num1 = int(operacao.split(tipo)[0])
num2 = int(operacao.split(tipo)[1])


dic = {'+':soma, '-':sub, '*':mult, '/':div}

z = dic[tipo](num1,num2)
print(z)


exit()

operacao = input('Entre com a operacao: ')
operadores ='+-*/'

#descobrir o operador


#MINHA FORMA
for k in operacao:
	if k in operadores:
		tipo = k

# achando os numeros
num1 = int(operacao.split(tipo)[0])
num2 = int(operacao.split(tipo)[1])

#calculando
if tipo == '+':
	calc = num1 + num2
if tipo == '-':
	calc = num1 - num2
if tipo == '*':
	calc = num1 * num2
if tipo == '/':
	calc = num1 / num2

print(calc)




