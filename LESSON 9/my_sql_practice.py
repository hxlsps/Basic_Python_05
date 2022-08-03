''' 
1. Create DB
a, Create a new database named VTI_Employees.
b, Create 2 tables:
- Table 1: Employee_Info
    + Emp_ID <Primary key>
    + Name
    + DoB
    + Email
    + MobileNumber

- Table 2: Employee_Work
    + Emp_ID <Foreign key>
    + Role
    + Department
    + Salary

2. Write the program to do following tasks:
a, Display the menu:
----------- Select Operation -------------
O_1. Display all employees information
O_2. Display employee information with specific Name
O_3. Insert a new employee
O_4. Update a specific employee with Emp_ID
O_5. Delete a specific employee with Emp_ID

b, Perform coresponding operations based on the user's choice.
'''
import mysql.connector

myconn = mysql.connector.connect(host = 'localhost', 
                                user = 'root', 
                                passwd = 'root',
                                database = 'VTI_Employees')

cur = myconn.cursor()

def create_database():
    cur.execute('CREATE DATABASE VTI_Employees')

#create_database()    

def create_table():
    cur.execute('''
        CREATE TABLE Employee_Info(
            Emp_ID INT PRIMARY KEY,
            Name VARCHAR(100),
            DoB DATE,
            Email VARCHAR(100),
            MobileNumber VARCHAR(10)
        )
    ''')

    cur.execute('''
        CREATE TABLE Employee_Work(
            Emp_ID INT,
            Role VARCHAR(100),
            Department INT,
            Salary INT,
            FOREIGN KEY (Emp_ID) REFERENCES Employee_Info(Emp_ID) ON UPDATE CASCADE ON DELETE CASCADE
        )
    ''')

#create_table()

def select_info():
    cur.execute('''
        SELECT * FROM Employee_Info ei
        JOIN Employee_Work ew ON ei.Emp_ID = ew.Emp_ID
    ''')

def info_emp_spec_name():
    cur().execute('''
        SELECT DISTINCT Name FROM Employee_Info
    ''')

def insert_new_emp():
    sql_e_info = ('''
        INSERT INTO Employee_Info(Emp_ID, Name, DoB, Email, MobileNumber)
        VALUES (%s, %s, %s, %s, %s)
    ''')
    vals_e_info = [
        (1,'loc','2000-04-11','abc@gmail.com','0936475161'),
        (2,'abc','1999-11-11','abcd@gmail.com','0912345678')
    ]

    sql_e_work = ('''
        INSERT INTO Employee_Work(Emp_ID, Role, Department, Salary)
        VALUES(%s, %s, %s, %s)
    ''')
    vals_e_work = [
        (1, 'dev', 10, 3000),
        (2, 'content', 20, 2000)
    ]

    cur.executemany(sql_e_info,vals_e_info)
    cur.executemany(sql_e_work,vals_e_work)
    myconn.commit()

#insert_new_emp()

def upd_spec_emp_by_ID(pre, after):
    sql = 'UPDATE Employee_Info SET Emp_ID = %s WHERE Emp_ID = %s'
    val = (after, pre)
    cur.execute(sql, val)
    myconn.commit()

#upd_spec_emp_by_ID(1,3)

def del_spec_emp_by_ID(input):
    sql = 'DELETE FROM Employee_Info WHERE Emp_ID = %s'
    val = (input, )
    cur.execute(sql, val)
    myconn.commit()

#del_spec_emp_by_ID(2)

myconn.close()
