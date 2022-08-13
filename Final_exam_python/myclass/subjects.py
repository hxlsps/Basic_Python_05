import mysql.connector
from sql import Mysql
from students import Student

class Subject(Student):
    def __init__(self):
        self.subject = Mysql()
        super().__init__()

    def insert(self):
        check = 'y'
        while check == 'y':
            subject_id = input('Input Subject ID: ')
            name = input('Input Subject Name: ')
            sql = ('''
                    INSERT INTO student(Subject_ID, Name)
                    VALUES (%s, %s)
                    ''')
            vals = (subject_id, name)
            self.subject.insert(sql, vals)
            print('Insert sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break

    def edit(self):
        check = 'y'
        while check == 'y':
            subject_info = input('Input Subject_ID or Name: ')
            print('''
                What do you want to change:
                1. Student ID
                2. Name
            ''')
            while True:
                try:
                    number = int(input('Input your choice (number 1 -2 ): '))
                    if number >= 1 and number <= 2:
                        break
                    else:
                        print('Only input 1 or 2')
                except:
                    print('Only input NUMBER 1 or 7!!!')
            message = input('Input what you want to change: ')
            if number == 1:
                execute = 'UPDATE subject SET Subject_ID = "{}" WHERE Subject_ID = "{}" or Name = "{}"'.format(message, subject_info, subject_info)
                self.subject.update_or_delete(execute)
            elif number == 2:
                execute = 'UPDATE subject SET Name = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, subject_info, subject_info)
                self.subject.update_or_delete(execute)
            
            print('Edit sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break

    def delete(self):
        check = 'y'
        while check == 'y':
            subject_info = input('Input Student_ID or Name: ')
            execute = 'DELETE FROM subject WHERE Student_ID ="{}" or Name ="{}"'.format(subject_info, subject_info)
            self.subject.update_or_delete(execute)
            print('Delete sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break


    def search(self):
        check = 'y'
        while check == 'y':
            print('''
                What do you want to search:
                1. Subject ID
                2. Name
            ''')
            while True:
                try:
                    number = int(input('Input your choice (number 1 or 2): '))
                    if number >= 1 and number <= 2:
                        break
                    else:
                        print('Only input 1 or 2')
                except:
                    print('Only input NUMBER 1 or 2!!!')
            message = input('Input the one you want to search: ')
            if number == 1:
                execute = 'SELECT * FROM subject WHERE Student_ID ="{}"'.format(message)
                self.subject.select(execute)
            elif number == 2:
                execute = 'SELECT * FROM subject WHERE Name ="{}"'.format(message)
                self.subject.select(execute)
            print('Search sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break