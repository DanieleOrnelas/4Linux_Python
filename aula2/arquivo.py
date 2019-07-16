#!/usr/bin/python3

arq = 'arquivo.txt'

nomes = ['\nRobin\n', 'Mulher Maravilha\n', 'Superman\n']

with open(arq,"w") as arquivo:
	arquivo.writelines(nomes)

with open(arq) as arquivo:
	conteudo = arquivo.read()
	print(conteudo)



exit()
arq = 'arquivo.txt'

with open(arq,"w") as arquivo:
	arquivo.write('Batman\n')

with open(arq) as arquivo:
	conteudo = arquivo.read()
	print(conteudo)

exit()
with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()
print(linhas)


exit()
with open('arquivo.txt') as arquivo:
	for linha in arquivo:
		print(linha)

exit()
# abrindo e fechando o arquivo automaticamente
with open('arquivo.txt') as arquivo:
	conteudo = arquivo.read()
	print(conteudo)

exit()

#Abrindo e fechando o arquivo manualmente
arquivo = open('arquivo.txt', "r")
print(arquivo.read())
arquivo.close()