#!/usr/bin/python3


#USANDO DO TUPLA - IGUAL A LISTA, MAS VC NÃO PODE ALTERAR NENHUM VALOR DELA

retangulo = (100,50)
print(retangulo[0],retangulo[1])
#retangulo[0] = 30
retangulo = (30,50)
print(retangulo[0],retangulo[1])

x = list(retangulo)
x[0] = 30
print(x)