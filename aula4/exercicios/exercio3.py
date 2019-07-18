#!/usr/bin/python3



from banco import Conta as CC
from banco import CP

def main():

	conta1 = CC('joao',30000)
	conta2 = CP('joao',0)
	conta3 = CC('maria',2000)

	conta1.transferir(3000,conta3)
	conta1.transferir(5000,conta2)
	conta2.render()

	conta1.verifica_saldo()
	conta2.verifica_saldo()
	conta3.verifica_saldo()

if __name__ == '__main__':
	main()

