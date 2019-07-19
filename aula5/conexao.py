import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='teste1', user='dornelas',
		password='Meteoro@123')
	# print('Conectou')
	cur = con.cursor()		# cursor, que permitirar executar comandos do BD

except Exception as e:
	print('Erro: {}'.format(e))