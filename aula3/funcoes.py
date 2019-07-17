#!/usr/bin/python3

exit()
#--------------------------------

def quadrado(n):
	return n ** 2

def raiz(n):
	return n ** (0.5)

f = [quadrado,raiz]

for k in range(0,26):										# %%%
	valores = list(map(lambda x : x(k), f))					# %%%
	print(valores)											# %%%

print('\n')

[print(list(map(lambda x : x(k), f))) for k in range(0,26)] # FORMA MAIS LIMPA 
															# DE ESCREVER O BLOCO ANTERIOR,
															# IDENT COM %%%



#--------------------------------

n1 = [1,2,3]
n2 = [4,5,6,]

r = list(map(lambda x,y : x * y, n1, n2))
print(r)


#--------------------------------
import math # Modulo matemático

l1 = [1,4,9,16,25]
l2 = list(map(math.sqrt, l1))
print(l2)

#--------------------------------
def dobro(n):
	return 2 * n

num = (1,2,3,4,5)
r = list(map(dobro,num)) 	# map é uma função nativa do python, pela qual aplica-se uma função 
							#para cada elemento de uma lista

r = list(map(lambda n : 2 * n, num)) # Usando funcao anonima

print(r)
#--------------------------------
# REFAZENDO A CALCULADORA USANDO FÇ ANONIMA
calcula = {
	'+' : lambda x,y : x + y,
	'-' : lambda x,y : x - y,
	'/' : lambda x,y : x / y,
	'*' : lambda x,y : x * y
}

#FUNCOES UTILIZADAS ANTERIORMENTES
	# def soma(num1,num2):
	# 	return num1 + num2
	# def sub(num1,num2):
	# 	return num1 - num2
	# def mult(num1,num2):
	# 	return num1 * num2
	# def div(num1,num2):
	# 	return num1 / num2


operacao = input('Entre com a operacao: ')
operadores ='+-*/'

for k in operacao:
	if k in operadores:
		tipo = k

# achando os numeros
num1 = int(operacao.split(tipo)[0])
num2 = int(operacao.split(tipo)[1])

print(calcula[tipo](num1,num2))

#--------------------------------
exit()
# def tamanho(frase):
# 	return[len(palavra) for palavra in frase]
tamanho = lambda frase : [len(palavra) for palavra in frase] # função anonima igual a funcao anterior

frase = 'joao foi para a escola'.split()
print(tamanho(frase))# RESULTADO ----> [4, 3, 4, 1, 6]


#--------------------------------
def multiplica(n):
	return lambda a : a * n

dobro = multiplica(2)
triplo = multiplica(3)

print(dobro(12))# RESULTADO ----> 24
print(triplo(12))# RESULTADO ----> 36


#--------------------------------
x = lambda a,b : a + b
a = x(5,3)
print(a)# RESULTADO ----> 8


#--------------------------------
def funcao(par1,par2):
	pass # Usabdo para passar adiante no código, sem dar erro. Usar quando ainda está construindo a função.


#EXEMPLO DE FUNCAO ANONIMA

def exemplo(a):
	return a + 10
x = lambda a : a + 10 # lambda é uma funcao anonima igualm a funcao anonima definida anteriormente
print(x(5)) # RESULTADO ----> 15

