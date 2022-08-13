import mysql.connector
from mysql.connector import Error

class Mysql:
    def __init__(self, myhost = 'localhost', myuser = 'root', mypasswd = 'root'):
        self.host = myhost
        self.user = myuser
        self.passwd = mypasswd
        self.__myconn = mysql.connector.connect(host = self.host,
                                                user = self.user,
                                                passwd = self.passwd)

    def connect(self, database_name = 'info_management'):
        try: 
            self.conn = mysql.connector.connect(host = self.host,
                                                user = self.user,
                                                passwd = self.passwd,
                                                database = database_name)
            return self.conn
        except:
            print('Error')
    
    def close(conn):
        if conn.is_connected():
            conn.close()

    def create_database(self, database_name = 'info_management'):
        try:
            if self.__myconn.is_connected():
                print('Connected')
                cur = self.__myconn.cursor()
                cur.execute('CREATE DATABASE {}'.format(database_name))
                print('Create database {} successfully'.format(database_name))
        except Error:
            print('Error: Database exists')
        finally:
            if self.__myconn.is_connected():
                self.__myconn.close()
    
    def create_table(self, database_name = 'info_management'):
        try:
            conn = self.connect(database_name)
            if conn.is_connected():
                execute = '''
                DROP TABLE IF EXISTS Student;
                CREATE TABLE Student(
                Student_ID VARCHAR(10) PRIMARY KEY,
                Name VARCHAR(50) NOT NULL,
                DoB DATE NOT NULL,
                Sex VARCHAR(10),
                Address VARCHAR(50),
                Mobile_Number VARCHAR(50) NOT NULL ,
                Email VARCHAR(50) UNIQUE KEY NOT NULL
                );

                DROP TABLE IF EXISTS Subject;
                CREATE TABLE Subject(
                Subject_ID VARCHAR(10) PRIMARY KEY,
                Name VARCHAR(50) NOT NULL
                );

                DROP TABLE IF EXISTS Score;
                CREATE TABLE Score(
                Student_ID VARCHAR(10),
                Subject_ID VARCHAR(10),
                Middle_Score INT,
                Final_Score INT,
                FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY(Subject_ID) REFERENCES Subject(Subject_ID) ON DELETE CASCADE ON UPDATE CASCADE
                );
                '''
                cur = conn.cursor()
                cur.execute(execute)
                print('Create tables successfully')
                conn.close()
        except Error:
            print('Table exists')
    
    def insert(self, sql, vals):
        try:
            conn = self.connect()
            if conn.is_connected():
                cur = conn.cursor()
                cur.execute(sql, vals)
                conn.commit()
                conn.close()
        except:
            print('Error')
        
    def update_or_delete(self, exe):
        try:
            conn = self.connect()
            if conn.is_connected():
                cur = conn.cursor()
                cur.execute(exe)
                conn.commit()
                conn.close()
        except:
            print('Error')
    
    def select(self, exe):
        try:
            conn = self.connect()
            if conn.is_connected():
                cur = conn.cursor()
                cur.execute(exe)
                result = cur.fetchall()
                for row in result:
                    print(row)
                conn.commit()
                conn.close()
        except:
            print('Error')



loc = Mysql()
loc.create_table()