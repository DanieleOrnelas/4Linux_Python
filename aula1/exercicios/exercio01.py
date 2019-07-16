#!/usr/bin/python3

# EXERCICIO 1
# Entrar com o nome e 4 notas de uma aluno usando input, calcular e mostrar na tela o nome e a meia das notas



nome = input('Entre com o nome do aluno: ')
nota1 = float(input('Entre com a primeira nota do aluno ' + nome + ': '))
nota2 = float(input('Entre com a primeira nota do aluno ' + nome + ': '))
nota3 = float(input('Entre com a primeira nota do aluno ' + nome + ': '))
nota4 = float(input('Entre com a primeira nota do aluno ' + nome + ': '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('A media das notas do aluno ' + nome + ' é: ' + str(media))

exit() #FORMA MANUAL ("BURRA") - OK
nome = input('Entre com o nome do aluno: ')
nota1 = input('Entre com a primeira nota do aluno ' + nome + ': ')
nota2 = input('Entre com a primeira nota do aluno ' + nome + ': ')
nota3 = input('Entre com a primeira nota do aluno ' + nome + ': ')
nota4 = input('Entre com a primeira nota do aluno ' + nome + ': ')
media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4
print('A media das notas do aluno ' + nome + ' é: ' + str(media))