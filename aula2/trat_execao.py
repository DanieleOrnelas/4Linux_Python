#!/usr/bin/python3

while True:

	try:
		n1 = int(input("Digite: "))
		n2 = int(input("Digite: "))
		r = n1/n2
	except ZeroDivisionError as e:
		print("Impossivel divir por zero")
	except NameError as e:
		print("Variavel inexistente")
	except ValueError as e:
		print("Digite apenas numeros")
		break
	else:
		print(r)





try:
	print(5/0)
except ZeroDivisionError as e:
	print("Erro: {}".format(e))