#!/usr/bin/python3



#NOVO EXEMPLO
herois = ['superman','batman','flash','mulher maravilha', 'robin', 'thor']
heroi = 'capitao america'

if heroi in herois:
	print(heroi, ' está na lista')
else:
	print(heroi, ' não está na lista')

for heroi in herois:
	print(heroi)

for k in range(1,10):
	print(k)

exit()

#NOVO EXEMPLO
valor = list(range(2,15))
print(valor)#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

soma = 0
n = 0
while n < len(valor):
	soma += valor[n] # soma = soma + valor[n]
	print(soma)
	n += 1 # n = n + 1
print('Media: {}'.format(soma / len(valor)))
'''
RESULTADO DOS ÚLTIMOS DOIS PRINTS ANTERIORES
2
5
9
14
20
27
35
44
54
65
77
90
104
Media: 8.0
'''



#NOVO EXEMPLO
herois = ['superman','batman','flash','mulher maravilha', 'robin', 'thor']

print(herois)
print(herois[1:4])
print(herois[:4])
print(herois[:4:2])
print(herois[1:-1])
print(herois[::-1])
'''
RESULTADO DOS SEIS PRINTS ANTERIORES
['superman', 'batman', 'flash', 'mulher maravilha', 'robin', 'thor']
['batman', 'flash', 'mulher maravilha']
['superman', 'batman', 'flash', 'mulher maravilha']
['superman', 'flash']
['batman', 'flash', 'mulher maravilha', 'robin']
['thor', 'robin', 'mulher maravilha', 'flash', 'batman', 'superman']
'''


#NOVO EXEMPLO
herois = ['superman','batman','flash','mulher maravilha']
herois.sort(reverse=True)#Ordena e modifica a lista
print(herois)#['superman', 'mulher maravilha', 'flash', 'batman']
print(sorted(herois))#ordena, porém, não modifica a lista ['batman', 'flash', 'mulher maravilha', 'superman']
print(herois)#['superman', 'mulher maravilha', 'flash', 'batman']



#NOVO EXEMPLO
herois = ['superman','batman','flash','mulher maravilha']#ìndice começa em 0
print(herois, len(herois))#len = tamanho da lista
print('-----')
herois[2] = 'arqueiro'
print(herois, len(herois))
herois.insert(2,'robin')
print('-----')
print(herois, len(herois))
print(herois.pop(), herois, len(herois))#pop - retirar item da lista, por defaut o último
print(herois.pop(0), herois, len(herois))
herois.remove('robin')
print(herois, len(herois))
herois.append('thor')
print(herois, len(herois))