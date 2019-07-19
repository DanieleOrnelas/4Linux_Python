

import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='teste1', user='dornelas',
		password='Meteoro@123')
	# print('Conectou')
	cur = con.cursor()		# cursor, que permitirar executar comandos do BD

except Exception as e:
	print('Erro: {}'.format(e))



def criar():
	cur.execute('create table usuarios(id int auto_increment primary key, ' +
			'nome varchar(50), cpf varchar(11), estado varchar (2));')

def dropar():
	cur.execute('drop table usuarios;')

def cadastrar():
		
	# cur.execute('insert into usuarios(nome,cpf,estado) values ' +
	# 	'(' + nome + ',' + cpf + ',' + estado + ');')
	cur.execute('insert into usuarios(nome,cpf,estado) values ' +
		'(\'{}\',\'{}\',\'{}\');'.format(nome,cpf,estado))


# def cadastrar(**kwargs):
# 	with open(arq,'a') as arquivo:
# 		arquivo.write("{}\t{}\t{}\n".format(kwargs['cpf'],kwargs['nome'],kwargs['estado']))
# 	print('\nCadastro adicionado!')


# def cadastrar(**kwargs):
# 	with open(arq,'a') as arquivo:
# 		arquivo.write("{}\t{}\t{}\n".format(kwargs['cpf'],kwargs['nome'],kwargs['estado']))
# 	print('\nCadastro adicionado!')

# def buscar(cpf):
# 	dic = {}
# 	k = 0
# 	chaved = ['cpf','estado','nome']

# 	with open(arq) as arquivo:
# 		for linha in arquivo:
# 			itens = linha.split('\t')
# 			itens[-1] = itens[-1][:-1]

# 			for item in itens:
# 				dic[chaved[k]] = item
# 				k =+ 1
# 				if k == 3:
# 					k = 0
			
# 			if dic[chaved[0]] == cpf:
# 				print("{}\t{}\t{}\n".format(dic['cpf'],dic['estado'],dic['nome']))
# 				return dic
# 			else:
# 				print('Cadastro nao encontrado')




while True:
	opt = int(input('Opcoes: \n 0 - Sair\n 1 - Buscar\n 2 - Cadastrar\n ' +
	'3 - Atualizar\n 4 - Deletar\n 5 - Criar tabela Usuarios\n 6 - Dropar ' +
	'Tabela Usuarios\n\n Escolha a opcao: '))

	if opt == 0: 
		exit()

	if opt == 2:
		lista = input('Digite nome-estado-cpf: ').split(',')
		nome=lista[0]
		estado=lista[1]
		cpf=lista[2]

		cadastrar()

		# cadastrar(nome=lista[0],estado=lista[1],cpf=lista[2])
		exit()

	if opt == 5:
		criar()
		exit()

	if opt == 6:
		dropar()
		exit()





		# cur.execute('select * from herois')

	# elif opt == 1:
	# 	lista = input('Digite nome-estado-cpf: ').split(',')
	# 	cadastrar(nome=lista[0],estado=lista[1],cpf=lista[2])
	# 	exit()
	# else:
	# 	cpf = input('Digite o cpf para busca: ')
	# 	buscar(cpf)
	# 	exit()








# # cur.execute('create table herois(id int auto_increment primary key, nome varchar(50), idade int);')

# # cur.execute('insert into herois(nome,idade) values (\'batman\',80);')
# # cur.execute('insert into herois(nome,idade) values (\'robin\',20);')
# # cur.execute('insert into herois(nome,idade) values (\'asa notuna\',30);')

# # cur.execute("update herois set nome='asa noturna' where nome='asa notuna';")

# cur.execute('select * from herois')
# # # RESULTADO será uma LISTA de TUPLAS (uma lista em que os valores de cada Id vem na forma de uma tupla
# # # [(3, 'charada', 32), (4, 'arlequina', 18), (5, 'mascara negra', 30), (1, 'coringa', 35), (6, 'coringa', 30)]

# print(cur.fetchone())
# print(cur.fetchall())


con.commit()	# Todoso os comandos executados no BD fora do terminal, precisam ser commitadot


cur.close()
con.close()
# cur.execute('\dt')
