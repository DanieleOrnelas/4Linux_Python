#!/usr/bin/python3

class Carro():
	def __init__(self, marca,modelo,ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0
		self.gasolina = 0

	def descrever(self):
		print('{} {}, {}'.format(self.marca,self.modelo,self.ano))

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

	def enche_tanque(self):
		self.gasolina = 100
		# print('Gasolina: {}'.format(self.gasolina))

class Bateria():
	def __init__(self, bateria = 100):
		self.bateria = bateria

	def descrever_bateria(self):
		print('	Carro com: {} de bateria'.format(self.bateria))

	def calculo_distancia(self):
		calculo_distancia = self.bateria * 2
		print(('	Este carro possui carga para ' +
			'{} km').format(calculo_distancia))


class Eletrico(Carro):
	def __init__(self, marca,modelo,ano):
		super().__init__(marca,modelo,ano)
		# self.bateria = 0
		self.bateria = Bateria(100)

	def enche_tanque(self):
		print('	Este carro é elétrico')


c1 = Carro('VW','fusca','1980')
c2 = Eletrico('Tesla','model s','2016')

c1.descrever()
print('	Carro com: {} de gasolina'.format(c1.gasolina))
c1.enche_tanque()
print('	Carro com: {} de gasolina'.format(c1.gasolina))
print('')
c2.descrever()
# c2.descrever_bateria()
# c2.enche_tanque()
# print('	Carro com: {} de bateria'.format(c2.gasolina))
c2.bateria.descrever_bateria()
c2.bateria.calculo_distancia()

