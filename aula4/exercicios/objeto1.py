#!/usr/bin/python3
# PROGRAMA PARA:

# Classe User
# ATRIBUTOS: Nome / Sobrenome / Username / Senha / Numero de Tentativas
# METODOS: Descrever / Saudacao / Login (usando input) / Incrementar tentativas / Reseta Tentativas


# PROGRAMA DO TIO
class Usuario():

	def __init__(self,nome,sobrenome,username,password):	
		self.nome = nome
		self.sobrenome = sobrenome
		self.username = username
		self.password = password
		self.tentativas = 0
		
		
	def descrever(self): 	
		print('Usuario {} pertence a {} {}\n'.format(self.username,self.nome,self.sobrenome))

	def saudar(self):
		print('	Bom dia {} {}\n'.format(self.nome,self.sobrenome))

	def reseta_tentativas(self):
		self.tentativas += 0
		exit()

	def incrementa_tentativas(self):
		self.tentativas += 1
		print('Número de tentativas: {}'.format(self.tentativas))


		
	def login(self):
		while self.tentativas <= 3:
			u = input('Entre com o usuario: ')
			s = input('Entre com a senha: ')
			if u == self.username and s == self.password:
				print('Login efetuado com sucesso')
				self.reseta_tentativas()
			else:
				self.incrementa_tentativas()
		exit()


dornelas = Usuario('Daniele','Ornelas','dornelas','123654')

while True:
	dornelas.login()

exit()
# MEU PROGRAMA
class Usuario():

	def __init__(self,nome,sobrenome,username,password):	
		self.nome = nome
		self.sobrenome = sobrenome
		self.username = username
		self.password = password
		self.tentativas = 3
		
	def descrever(self): 	
		print('Usuario {} pertence a {} {}\n'.format(self.username,self.nome,self.sobrenome))

	def saudar(self):
		print('	Bom dia {} {}\n'.format(self.nome,self.sobrenome))

	def login(self):
		t = 1
		while t <= self.tentativas:
			u = input('Entre com o usuario: ')
			s = input('Entre com a senha: ')
			if u == self.username and s == self.password:
				print('Login efetuado com sucesso')
				exit()
			else:
				x = self.tentativas - t
				if x != 0:
					print('Usuario ou senha incorretos. Tentativas restantes: ', x)
				else:
					print('Número de tentativas esgotadas!')
				t += 1


dornelas = Usuario('Daniele','Ornelas','dornelas','123654')
# dornelas.descrever()
# dornelas.saudar()
dornelas.login()


