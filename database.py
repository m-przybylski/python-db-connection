host = '192.168.2.81'
port = 5432
user = 'postgres'
passwd = 'postgres123'
dbname = 'lamassu'

from pg import DB
db = DB(dbname, host, port, user = user, passwd = passwd)
print(db.query('select * from customers'))
