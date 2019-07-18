#!/usr/bin/python3

class Conta():
	def __init__(self,correntista,saldo,tipo,status):
		self.correntista = correntista
		self.saldo = saldo
		self.tipo = tipo
		self.status = status

	def verifica_saldo(self):
		print('Saldo da CC de {} é: {}'.format(self.correntista,self.saldo))
	
	def transferencia(self,transf):
		if self.status == 'sacado':
			self.saldo = self.saldo - transf
			print('Saldo de {} é: {}'.format(self.correntista,self.saldo))
		else:
			self.saldo = self.saldo + transf
			print('Saldo de {} é: {}'.format(self.correntista,self.saldo))
		
	def saque(self,saque):
		self.saldo = self.saldo - saque

	def deposito(self,deposit):
		self.saldo = self.saldo + deposit


class CP():
	def __init__(self,correntista,saldo,tipo):
		self.correntista = correntista
		self.saldo = saldo
		self.tipo = tipo

	def verifica_saldo(self):
		print('Saldo da CP de {} é: {}'.format(self.correntista,self.saldo))
	
	def transferencia(self,transf=3000):
		pass 

	def saque(self):
		pass

	def deposito(self):
		pass

conta1 = Conta('joao',30000,'cc','sacado')
conta2 = Conta('joao',0,'cp','credito')
conta3 = Conta('maria',2000,'cc','credito')


conta1.transferencia(3000)
conta2.transferencia(3000)