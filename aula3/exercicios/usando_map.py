#!/usr/bin/python3

# TRANSFORMAR FAHRENHEIT PARA CELSIUS E VICE E VERSA
# USANDO MAP
# USANDO LAMBDA + MAP


operacao = input('Converter: \n C -> F, digite C \n F -> C, digite F\n\n').lower()

temp = (15,16,17,18,19,20)


if operacao == 'c':
	t = list(map(lambda n : (9/5) * n + 32,temp))
	print(t)
elif operacao == 'f':
	t = list(map(lambda n : (5/9) * (n - 32),temp))
	print(t)



exit()

def celsius(n):
	return (9/5) * n + 32

def fahrenheit(n):
	return (5/9) * (n - 32)

operacao = input('Converter: \n C -> F, digite C \n F -> C, digite F\n\n').lower()

temp = (15,16,17,18,19,20)

if operacao == 'c':
	t = list(map(celsius,temp))
	print(t)
elif operacao == 'f':
	t = list(map(fahrenheit,temp))
	print(t)

