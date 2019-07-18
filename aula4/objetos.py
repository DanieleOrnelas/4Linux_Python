#!/usr/bin/python3

# Uma classe associa dados (atributos) e operações (métodos) numa só estrutura.
# Um objeto é uma instância de uma classe - uma representação da classe.

class Carro():
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0

	def descrever(self):
		print('{} {} {}'.format(self.marca,self.modelo,self.ano))

	def ler_hodometro(self):
		print('Este carro rodou {} km'.format(self.hodometro))

	def atualiza_hodometro(self,kms):
		if kms >= self.hodometro:
			self.hodometro = kms

	def incrementa_hodometro(self,kms):
		if kms >= 0:
			self.hodometro += kms
		else:
			print('Não é possível diminuir km')

meu_carro = Carro('VW','fusca','1980')
meu_carro.descrever()
meu_carro.atualiza_hodometro(50)
meu_carro.ler_hodometro()
meu_carro.incrementa_hodometro(50)
meu_carro.ler_hodometro()

		


exit()
class Restaurantes():
	
	def __init__(self, nome, tipo, aberto):
		self.nome = nome
		self.tipo = tipo
		self.aberto = aberto

	def descrever(self):
		print(('{}  é um restaurante de ' +
			'comida {}').format(
			self.nome,self.tipo,self.aberto))

	def status(self):
		if self.aberto == True:
			print ('	Está aberto'.format(self.nome))
		else:
			print ('	Está fechado'.format(self.nome))

primeiro = Restaurantes('Mcdonalds','fast food',
	True)
segundo = Restaurantes('Outback', 'australiana',
	False)
terceiro = Restaurantes('Marianas', 'brasileira',
	False)

primeiro.descrever()
primeiro.status()

segundo.descrever()
segundo.status()

terceiro.descrever()
terceiro.status()


		

exit()
class Usuario():

	def __init__(self,nome,sobrenome):	
		self.nome = nome
		self.sobrenome = sobrenome

	def descrever(self): 	
		print('Nome do usuario: {} {}\n'.format(self.nome,self.sobrenome))

	def saudar(self):
		print('	Bom dia {} {}\n'.format(self.nome,self.sobrenome))


dornelas = Usuario('Daniele','Ornelas')
pclyra = Usuario('Andre','Lyra')

dornelas.descrever()
dornelas.saudar()

pclyra.descrever()
pclyra.saudar()

exit()
class Cachorro():
	""" Para class usar primeira letra em maiusculo no nome da classe"""

	dono = None

	def __init__(self,nome,idade):	# Definição dos atributos desta classe e todo metodo criado dentro de uma classe deve definir como primeiro parametro o self.
		self.nome = nome
		self.idade = idade

	def descrever(self):		# Definição das funções ou métodos da classe
		print('nome: {}\nidade: {}'.format(self.nome,self.idade))

	def sentar(self):
		print('{} está sentado'.format(self.nome))

	def rolar(self):
		print(('{} está rolando de um lado' + ' para o outro').format(self.nome))

meu_cachorro = Cachorro('jake',2)
print('O dono é {}'.format(meu_cachorro.dono))
meu_cachorro.dono = 'joao'
meu_cachorro.descrever()
print('O dono é {}'.format(meu_cachorro.dono))
meu_cachorro.sentar()
meu_cachorro.rolar()

