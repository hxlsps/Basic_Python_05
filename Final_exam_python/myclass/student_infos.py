from sql import Mysql
from students import Student

class Student_Info(Student):
    def __init__(self):
        self.student = Mysql()
        super().__init__()

    def insert(self):
        check = 'y'
        while check == 'y':
            student_id = input('Input Student_ID: ')
            name = input('Input Name: ')
            dob = input('Input Date of Birth: ')
            sex = input('Input Sex: ')
            address = input('Input Address: ')
            mobile_number = input('Input Mobile Number: ')
            email = input('Input email: ')
            sql = ('''
                    INSERT INTO student(Student_ID, Name, DoB, Sex, Address, Mobile_Number, Email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ''')
            vals = (student_id, name, dob, sex, address, mobile_number, email)
            self.student.insert(sql, vals)
            print('Insert sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break
    
    def edit(self):
        check = 'y'
        while check == 'y':
            student_info = input('Input Student_ID or Name: ')
            print('''
                What do you want to change:
                1. Student ID
                2. Name
                3. Date of Birth
                4. Sex
                5. Address
                6. Mobile Number
                7. Email
            ''')
            while True:
                try:
                    number = int(input('Input your choice (number from 1 to 7): '))
                    if number >= 1 and number <= 7:
                        break
                    else:
                        print('Only input from 1 to 7')
                except:
                    print('Only input NUMBER from 1 to 7!!!')
            message = input('Input what you want to change: ')
            if number == 1:
                execute = 'UPDATE student SET Student_ID = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            elif number == 2:
                execute = 'UPDATE student SET Name = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            elif number == 3:
                execute = 'UPDATE student SET DoB = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            elif number == 4:
                execute = 'UPDATE student SET Sex = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            elif number == 5:
                execute = 'UPDATE student SET Address = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            elif number == 6:
                execute = 'UPDATE student SET Mobile_Number = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            elif number == 7:
                execute = 'UPDATE student SET Email = "{}" WHERE Student_ID = "{}" or Name = "{}"'.format(message, student_info, student_info)
                self.student.update_or_delete(execute)
            
            print('Edit sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break

    def delete(self):
        check = 'y'
        while check == 'y':
            student_info = input('Input Student_ID or Name: ')
            execute = 'DELETE FROM student WHERE Student_ID ="{}" or Name ="{}"'.format(student_info, student_info)
            self.student.update_or_delete(execute)
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
                1. Student ID
                2. Name
                3. Email
            ''')
            while True:
                try:
                    number = int(input('Input your choice (number from 1 to 3): '))
                    if number >= 1 and number <= 3:
                        break
                    else:
                        print('Only input from 1 to 3')
                except:
                    print('Only input NUMBER from 1 to 3!!!')
            message = input('Input the one you want to search: ')
            if number == 1:
                execute = 'SELECT * FROM student WHERE Student_ID ="{}"'.format(message)
                self.student.select(execute)
            elif number == 2:
                execute = 'SELECT * FROM student WHERE Name ="{}"'.format(message)
                self.student.select(execute)
            elif number == 3:
                execute = 'SELECT * FROM student WHERE Email ="{}"'.format(message)
                self.student.select(execute)
            print('Search sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break
