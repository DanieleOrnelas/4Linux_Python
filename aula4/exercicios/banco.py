#!/usr/bin/python3



class Conta():
	def __init__(self,correntista,saldo):
		self.correntista = correntista
		self.saldo = saldo


	def verifica_saldo(self):
		print('Saldo da CC de {} é: {}'.format(self.correntista,self.saldo))
	
	def saque(self,valor):
		self.saldo -= valor
		return self.saldo

	def deposito(self,valor):
		self.saldo += valor
		return self.saldo

	def transferir(self,valor,conta):
		self.saque(valor)
		conta.deposito(valor)
		

class CP(Conta):

	def __init__(self,correntista,saldo):
		super().__init__(correntista,saldo)
		self.juros = 1.006

	def verifica_saldo(self):
		print('Saldo da CP de {} é: {}'.format(self.correntista,self.saldo))
	
	def render(self):
		self.saldo *= self.juros
		return self.saldo




