#!/usr/bin/python3

notas = {'C':264,'D':297,'E':330,'F':352,'G':396,'A':440,'B':495,'C2':528}

def qual_nota(n):
	for chave,valor in notas.items():
		if n == valor:
			print('nota: {}'.format(chave))
			return True

	return False