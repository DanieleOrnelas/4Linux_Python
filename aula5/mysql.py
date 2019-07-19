

import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='teste1', user='dornelas',
		password='Meteoro@123')
	# print('Conectou')
	cur = con.cursor()		# cursor, que permitirar executar comandos do BD

except Exception as e:
	print('Erro: {}'.format(e))

# cur.execute('create table herois(id int auto_increment primary key, nome varchar(50), idade int);')

# cur.execute('insert into herois(nome,idade) values (\'batman\',80);')
# cur.execute('insert into herois(nome,idade) values (\'robin\',20);')
# cur.execute('insert into herois(nome,idade) values (\'asa notuna\',30);')

# cur.execute("update herois set nome='asa noturna' where nome='asa notuna';")

cur.execute('select * from herois')
# # RESULTADO será uma LISTA de TUPLAS (uma lista em que os valores de cada Id vem na forma de uma tupla
# # [(3, 'charada', 32), (4, 'arlequina', 18), (5, 'mascara negra', 30), (1, 'coringa', 35), (6, 'coringa', 30)]

print(cur.fetchone())
print(cur.fetchall())


con.commit()	# Todoso os comandos executados no BD fora do terminal, precisam ser commitadot


cur.close()
con.close()
# cur.execute('\dt')
