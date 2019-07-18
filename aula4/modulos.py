#!/usr/bin/python3

import time, random		# Importacao do modulo inteiro
from datetime import datetime	
from subprocess import run, PIPE	# Importacao de uma pedaço (run ou PIPE) de um modulo (subprocess)
from dir_modules.som import qual_nota

b = False

while b == False:
	f = random.randint(264,528)
	b = qual_nota(f)
	# Pode chamar a funcao diretamente, pq usou o from - import



exit()
r = run(['apt','instal','-y','sl'], stdout=	PIPE, stderr=PIPE)
# print(r)
r = run(['ls','-l'], stdout=PIPE, stderr=PIPE)
# print(r)

if r.returncode != 0:
	print('Deu ruim')
else:
	print('ok')

k = 0
while k != 505:
	k = random.randint(400,999)
	# print(k)

vogais = 'aeiouAEIOU'
print(random.choice(vogais))
time.sleep(3)
print(random.choice(vogais))
print(datetime.now())