#!/usr/bin/python3

# EXERCICIO 1
# Entrar com o nome e 4 notas de uma aluno usando input, calcular e mostrar na tela o nome e a meia das notas
# Se media >= 7 - APROVADO
# Se media < 5 - REPROVADO
# Se 5 <= media < 7 - RECUPERACAO. ENTRA NOVA NOTA. RECALCULA A MEDIA.
# Se media >= 5 - APROVADO
# Se media < 5 - REPROVADO

i = 1

nome = input('Entre com o nome do aluno: ')
soma = 0
nota = 0
while (i < 5):
	nota = float(input('Entre com a nota do aluno ' + nome + ': '))
	soma = soma + nota
	i += 1

media = soma / (i - 1)
print('A media das notas do aluno ' + nome + ' é: ' + str(media))

if media >= 7:
	print('Parabéns ' + nome + '. Você está aprovado')
elif media >= 5:
	nota = float(input('Entre com a nota de recuperação do aluno ' + nome + ': '))
	media = (media + nota) / 2
	if media >= 5:
		print('Parabéns ' + nome + '. Você está aprovado\n\tSua média foi: {}'.format(media))
	else:
		print(nome + ' você está reprovado')	
else:
	print(nome + ' você está reprovado')