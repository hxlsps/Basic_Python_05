from myclass.sql import Mysql
from myclass.scores import Score
from myclass.student_infos import Student_Info
from myclass.subjects import Subject

def main():
    check = 'y'
    while check == 'y':
        print('''
            What do you want to do?
            1 - Manage Students' Information
            2 - Manage Subject
            3 - Manage Students' Scores
            4 - Exit
            ''')
        while True:
            try: 
                choice = int(input('Input your answer (from 1 to 4): '))
                if choice >= 1 and choice <= 4:
                    break
                else:
                    print('Only input from 1 to 4')
            except:
                print('Only input NUMBER from 1 to 4.')
        if choice == 1:
            student_main()
            while True:
                check = input('Do you want to continue (y for yes, n for no): ')
                if check != 'y' and check != 'n':
                    print('Only input y or n!!!')
                else:
                    break
        elif choice == 2:
            subject_main()
            while True:
                check = input('Do you want to continue (y for yes, n for no): ')
                if check != 'y' and check != 'n':
                    print('Only input y or n!!!')
                else:
                    break
        elif choice == 3:
            score_main()
            while True:
                check = input('Do you want to continue (y for yes, n for no): ')
                if check != 'y' and check != 'n':
                    print('Only input y or n!!!')
                else:
                    break
        elif choice == 4:
            break

def student_main():
    check = 'y'
    while check == 'y':
        print('''
            What do you want to do?
            1 - Insert Student
            2 - Edit Student
            3 - Delete Student
            4 - Search Student by Student_ID, Name, Email
            ''')
        while True:
            try: 
                choice = int(input('Input your answer (from 1 to 4): '))
                if choice >= 1 and choice <= 4:
                    break
                else:
                    print('Only input from 1 to 4')
            except:
                print('Only input NUMBER from 1 to 4.')
    student = Student_Info()
    if choice == 1:
        student.insert()
    elif choice == 2:
        student.edit()
    elif choice == 3:
        student.delete()
    elif choice == 4:
        student.search()
    
def subject_main():
    check = 'y'
    while check == 'y':
        print('''
            What do you want to do?
            1 - Insert Subject
            2 - Edit Subject
            3 - Delete Subject
            4 - Search Subject by Subject_ID, Name
            ''')
        while True:
            try: 
                choice = int(input('Input your answer (from 1 to 4): '))
                if choice >= 1 and choice <= 4:
                    break
                else:
                    print('Only input from 1 to 4')
            except:
                print('Only input NUMBER from 1 to 4.')
    subject = Subject()
    if choice == 1:
        subject.insert()
    elif choice == 2:
        subject.edit()
    elif choice == 3:
        subject.delete()
    elif choice == 4:
        subject.search()

def score_main():
    check = 'y'
    while check == 'y':
        print('''
            What do you want to do?
            1 - Insert Score
            2 - Edit Score
            3 - Delete Score
            4 - Search Subject by Student_ID, Subject_ID
            5 - Calculate Avarage by Student_ID, Subject_ID
            6 - Making Stats
            ''')
        while True:
            try: 
                choice = int(input('Input your answer (from 1 to 6): '))
                if choice >= 1 and choice <= 6:
                    break
                else:
                    print('Only input from 1 to 6')
            except:
                print('Only input NUMBER from 1 to 6.')
    score = Score()
    if choice == 1:
        score.insert()
    elif choice == 2:
        score.edit()
    elif choice == 3:
        score.delete()
    elif choice == 4:
        score.search()
    elif choice == 5:
        score.average()
    elif choice == 6:
        score.make_stats()

main()

