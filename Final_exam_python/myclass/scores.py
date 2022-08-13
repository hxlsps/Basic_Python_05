import mysql.connector
from sql import Mysql
from students import Student

class Score(Student):
    def __init__(self):
        self.score = Mysql()
        super().__init__()
                    
    def insert(self):
        check = 'y'
        while check == 'y':
            student_id = input('Input Student_ID: ')
            subject_id = input('Input Subject_ID: ')
            while True:
                try:
                    middle_score = input('Input Middle Score: ')
                    break
                except:
                    print('Middle score must be integer.')
            while True:
                try:
                    final_score = input('Input Final Score: ')
                    break
                except:
                    print('Middle score must be integer.')
            sql = ('''
                    INSERT INTO student(Student_ID, Subject_ID, Middle_Score, Final_Score)
                    VALUES (%s, %s, %s, %s)
                    ''')
            vals = (student_id, subject_id, middle_score, final_score)
            self.score.insert(sql, vals)
            print('Insert sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break


    def edit(self):
        check = 'y'
        while check == 'y':
            score_info = input('Input Subject_ID or Student_ID: ')
            print('''
                What do you want to change:
                1. Student ID
                2. Subject_ID
                3. Middle Score
                4. Final Score
            ''')
            while True:
                try:
                    number = int(input('Input your choice (number from 1 to 4 ): '))
                    if number >= 1 and number <= 4:
                        break
                    else:
                        print('Only input number from 1 to 4')
                except:
                    print('Only input NUMBER 1 or 4!!!')
            message = input('Input what you want to change: ')
            if number == 1:
                execute = 'UPDATE subject SET Student_ID = "{}" WHERE Subject_ID = "{}" or Student_ID = "{}"'.format(message, score_info, score_info)
                self.score.update_or_delete(execute)
            elif number == 2:
                execute = 'UPDATE subject SET Subject_ID = "{}" WHERE Student_ID = "{}" or Student_ID = "{}"'.format(message, score_info, score_info)
                self.score.update_or_delete(execute)
            elif number == 3:
                execute = 'UPDATE subject SET Middle_Score = "{}" WHERE Student_ID = "{}" or Student_ID = "{}"'.format(message, score_info, score_info)
                self.score.update_or_delete(execute)
            elif number == 4:
                execute = 'UPDATE subject SET Final_Score = "{}" WHERE Student_ID = "{}" or Student_ID = "{}"'.format(message, score_info, score_info)
                self.score.update_or_delete(execute)
            
            print('Edit sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break

    def delete(self):
        check = 'y'
        while check == 'y':
            student_id = input('Input Student_ID: ')
            subject_id = input('Input Subject_ID: ')
            execute = 'DELETE FROM student WHERE Student_ID ="{}" and Name ="{}"'.format(student_id, subject_id)
            self.score.update_or_delete(execute)
            print('Delete sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break

    def search(self):
        check = 'y'
        while check == 'y':
            student_id = input('Input Student_ID: ')
            subject_id = input('Input Subject_ID: ')
            print('''
                What do you want to search:
                1. Middle Score
                2. Final Score
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
            if number == 1:
                execute = 'SELECT "{}" FROM subject WHERE Student_ID ="{}" and Subject_ID = "{}"'.format('Middle_Score', student_id, subject_id)
                self.score.select(execute)
            elif number == 2:
                execute = 'SELECT "{}" FROM subject WHERE Student_ID ="{}" and Subject_ID = "{}"'.format('Final_Score', student_id, subject_id)
                self.score.select(execute)
            print('Search sucessfully!')             
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break
    
    def average(self):
        check = 'y'
        while check == 'y':
            student_id = input('Input Student_ID: ')
            subject_id = input('Input Subject_ID: ')
            execute = 'SELECT (Middle_Score + Final_Score*2)/3 FROM subject WHERE Student_ID ="{}" and Subject_ID = "{}"'.format(student_id, subject_id)
            self.score.select(execute)                    
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break
    
    def make_stats(self):
        check = 'y'
        while check == 'y':
            pass
            check = input('Do you want to continue (y for yes, n for no): ')
            if check != 'y' and check != 'n':
                print('Only input y or n!!!')
            else:
                break
Loc = Score()
