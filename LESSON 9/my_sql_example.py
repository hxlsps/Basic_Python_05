import mysql.connector

myconn = mysql.connector.connect(host = 'localhost', 
                                user = 'root', 
                                passwd = 'root',
                                database = 'testdb')

print('Connected to MySQL Database')

cur = myconn.cursor()
#cur.execute('create database testdb')
cur.execute('show databases')
for row in cur:
    print(row)

#cur.execute('''
#    CREATE TABLE Employee(
#        Code VARCHAR(10) PRIMARY KEY,
#        Name VARCHAR(50) NOT NULL,
#        Salary FLOAT NOT NULL,
#        Department VARCHAR(100) NOT NULL
#    )
#''')

sql = '''
    INSERT INTO Employee(Code, Name, Salary, Department)
    VALUES(%s, %s, %s, %s)
'''
vals = ('PY0007', 'Loc', 500, 'Python 05')
cur.execute(sql, vals)
myconn.commit 

myconn.close()