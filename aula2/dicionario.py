#!/usr/bin/python3

#EXEMPLOS DO USO DE DICIONÁRIOS, COM SUAS CHAVES, VALORES, ITENS


herois = {
'batman':{'identidade':'bruce wane', 'cidade':'gotham'},
'superman':{'identidade':'clark kent', 'cidade':'metropilis'}
}

print(herois['batman']['identidade'])


exit()

lanche = {'pao':['integral', '4 queijos', 'italiano'], 'queijo':['prato', 'suico', 'cheddar'], 'recheio':['frango', 'carne', 'almondega']}

print(lanche['pao'][2])


exit()

koppa1 = {'cor':'vermelho', 'pontos':30}
koppa2 = {'cor':'verde', 'pontos':50}
koppa3 = {'cor':'azul', 'pontos':100}

koppa = [koppa1, koppa2, koppa3]
print(koppa[1]['cor'])

lista = []

for k in range(10):
	lista.append(koppa1)

print(lista)



exit()

usuario = {'username':'exemplo1', 'nome':'joao', 'sobrenome':'silva'}

print(usuario)

for chave,valor in usuario.items():
	print('chave: {}'.format(chave))
	print('valor: {}'.format(valor))

for chave in usuario.keys():
	print('chave: {}'.format(chave))

for valor in usuario.values():
	print('valor: {}'.format(valor))

exit()

#cores = {'red':'vermelho', 'blue':'azul', 'green':'verde'}
#print(cores['red'])

koppa1 = {'cor':'vermelho', 'pontos':30}
pontos = koppa1['pontos']

koppa1['eixo_x'] = 5
koppa1['eixo_y'] = 15
koppa1['velocidade'] = 'rapido'

print(koppa1)

if koppa1['velocidade']=='lento':
	anda_x = 1
elif koppa1['velocidade']=='medio':
	anda_x = 2
else:
	anda_x = 3

koppa1['eixo_x'] += anda_x
print(koppa1)


