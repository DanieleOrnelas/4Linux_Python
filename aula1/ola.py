#!/usr/bin/python3

exit()#Função para parar de executar a partir deste ponto

#NOVO EXEMPLO
nome = input('Digite o nome: ')#input para usuario entrar com o valor da variavel, por padrão uma STRING
idade = int(input('Digite idade: '))#int define a variavel como inteira
mensagem = nome.title() + ' tem ' + str(idade) + ' anos'#str para converter a variavel INT para STRING
print(mensagem)


# NOVO EXEMPLO
nome,sobrenome = 'daniele','ornelas'
print(nome.title() + ' ' + sobrenome.title())


# NOVO EXEMPLO
a,b = 10,3
print(a*b)


# NOVO EXEMPLO
nome = 'joao'
idade = 20
mensagem = nome.title() + ' tem ' + str(idade) + ' anos'#str para converter a variavel INT para STRING
print(mensagem)


nome = 'mcdonald\'s\n\t'#\ para interpretar o próximo caracter como fazendo parte da varuavel
						#\n para ir para próxima linha
						#\t para dar TAB 
sobrenome = "ornelas"
completo = nome.title() + sobrenome.title()
print(completo)

# NOVO EXEMPLO
nome = 'daniele'
sobrenome = "ornelas"
completo = nome.title() + ' ' + sobrenome.title()
print(completo)


# NOVO EXEMPLO
nome = '     mAddog   '
print(nome.split()) #Elimina espaços
print(nome.title()) #MAIUSCULO
print(nome.upper())
print(nome.strip())
print(nome.rstrip())
print(nome.lower())#minusculo


# NOVO EXEMPLO
mensagem = 'Hello Word!!!'
print (mensagem)
mensagem = 'Bem Vindo!!!'
print (mensagem)