#!/usr/bin/python3

arq = 'cadastro.txt'

# PROGRAMA DO TIO
def cadastrar(**kwargs):
	with open(arq,'a') as arquivo:
		arquivo.write("{}\t{}\t{}\n".format(kwargs['cpf'],kwargs['nome'],kwargs['estado']))
	print('\nCadastro adicionado!')

def buscar(cpf):
	dic = {}
	k = 0
	chaved = ['cpf','estado','nome']

	with open(arq) as arquivo:
		for linha in arquivo:
			itens = linha.split('\t')
			itens[-1] = itens[-1][:-1]

			for item in itens:
				dic[chaved[k]] = item
				k =+ 1
				if k == 3:
					k = 0
			
			if dic[chaved[0]] == cpf:
				print("{}\t{}\t{}\n".format(dic['cpf'],dic['estado'],dic['nome']))
				return dic
			else:
				print('Cadastro nao encontrado')




while True:
	opt = int(input('Opcoes: \n 0 - Sair\n 1 - Cadastrar\n 2 - Buscar\n\n Escolha a opcao: '))

	if opt == 0: 
		exit()
		# break
	elif opt == 1:
		lista = input('Digite nome-estado-cpf: ').split(',')
		cadastrar(nome=lista[0],estado=lista[1],cpf=lista[2])
		exit()
	else:
		cpf = input('Digite o cpf para busca: ')
		buscar(cpf)
		exit()


		# # MINHA TENTATIVA INUTIL
		# busca = str(input('Digite cpf para busca: '))
		# with open(arq) as arquivo:
				
		# 		for line in arquivo:
		# 			k = line[0:11]
		# 			# print(k)
		# 			# print(busca)
		# 			if k == busca:
		# 				print('cpf existe')
		# 				exit()
							
		# 			# print('cpf nao existe')
		# 			# exit()			
			
					
				






# # MEU PROGRAMA
# arq = 'cadastro.txt'
# arquivo = open('cadastro.txt', "a")
# opcao = input('Entre com a opção desejada.\n (0) para Sair\n (1) para Novo Cadastro\n (2) para Busca\n ')
# x = '#'
# y = "@"
# z = '&'

# if opcao == '1':
# 	print('Iniciando Novo Cadastro')
# 	nome = input('Nome: ')
# 	cpf = input('CPF: ')
# 	uf = input('UF: ')
# 	novo_cadastro = (nome,cpf,uf)
# 	print(novo_cadastro)
# 	with open(arq,"a") as arquivo:
# 		arquivo.write('{}'.format(novo_cadastro))
# 		arquivo.write('\n')

# elif opcao == '2':
# 	cpf = input('Entre com o cpf para busca: ')
# 	with open(arq,"a") as arquivo:
# 		linha = arquivo.readlines()
# 		if cpf in linha:
# 			print(linha)

