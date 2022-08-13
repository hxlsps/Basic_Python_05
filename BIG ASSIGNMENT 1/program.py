from abc import ABC, abstractmethod
import json

class Student(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def search(self):
        pass
    
    def _load_json(file):
        with open(file,'r',encoding='utf-8') as f:
            json_ob=json.load(f)
        return json_ob
    
    def _write_json(file,ob):
        with open(file,'w', encoding='utf-8') as f:
            json.dump(ob,f)

    
class Student_info(Student):
    def __init__(self):
        self.students = Student._load_json('students.json')['students']['student']
        super().__init__()
    
    def get_student_index(self, student_info):
        for index, student in enumerate(self.students):
            if student['Student_ID'] == student_info or student['Name'] == student_info:
                return index
    
    def _insert_of_edit_json(self):
        student_dict = Student._load_json('students.json')
        student_dict['students'] = {'student': self.students}
        return student_dict
    
    def get_info(self):
        check = 'y'
        while check == 'y':
            info = input('Input student ID or student\'s name: ')
            print(self.students[self.get_student_index(info)])
            check = input('Do you want to continue (y/n): ')

    def insert(self):
        check = 'y'
        while check == 'y':
            user1 = dict()
            user1['Student_ID'] = input('Input student ID: ')
            user1['Name'] = input('Input student\'s name: ')
            user1['DoB'] = input('Input student\'s date of birth: ')
            user1['Sex'] = input('Input student\'s sex: ')
            user1['Address'] = input('Input student\'s address: ')
            user1['Mobile_Number'] = input('Input student\'s mobile number: ')
            user1['Email'] = input('Input student\'s email: ')
            self.students.append(user1)
            Student._write_json('students.json', self._insert_of_edit_json())
            check = input('Do you want to continue (y/n): ')

    def edit(self):
        check = 'y'
        while check == 'y':
            info = input('Input student ID or student\'s name: ')
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
            number = int(input('Input your choice: '))
            message = input('Input what you want to change: ')
            if number == 1:
                self.students[self.get_student_index(info)]['Student_ID'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 2:
                self.students[self.get_student_index(info)]['Name'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 3:
                self.students[self.get_student_index(info)]['DoB'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 4:
                self.students[self.get_student_index(info)]['Sex'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 5:
                self.students[self.get_student_index(info)]['Address'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 6:
                self.students[self.get_student_index(info)]['Mobile_Number'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 7:
                self.students[self.get_student_index(info)]['Email'] = message
                Student._write_json('students.json', self._insert_of_edit_json())

            check = input('Do you want to continue (y/n): ')
        

    def delete(self):
        check = 'y'
        while check == 'y':
            info = input('Input student ID or student\'s name: ')
            print('''
                What do you want to delete:
                1. Student ID
                2. Name
                3. Date of Birth
                4. Sex
                5. Address
                6. Mobile Number
                7. Email
            ''')
            number = int(input('Input your choice: '))
            message = ''
            if number == 1:
                self.students[self.get_student_index(info)]['Student_ID'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 2:
                self.students[self.get_student_index(info)]['Name'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 3:
                self.students[self.get_student_index(info)]['DoB'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 4:
                self.students[self.get_student_index(info)]['Sex'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 5:
                self.students[self.get_student_index(info)]['Address'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 6:
                self.students[self.get_student_index(info)]['Mobile_Number'] = message
                Student._write_json('students.json', self._insert_of_edit_json())
            elif number == 7:
                self.students[self.get_student_index(info)]['Email'] = message
                Student._write_json('students.json', self._insert_of_edit_json())

            check = input('Do you want to continue (y/n): ')

    def search(self):
        check = 'y'
        while check == 'y':
            info = input('Input student ID or student\'s name: ')
            print('''
                What are you looking for:
                1. Student ID
                2. Name
                3. Date of Birth
                4. Sex
                5. Address
                6. Mobile Number
                7. Email
            ''')
            number = int(input('Input your choice: '))
            if number == 1:
                print(self.students[self.get_student_index(info)]['Student_ID'] )
            elif number == 2:
                print(self.students[self.get_student_index(info)]['Name'] )
            elif number == 3:
                print(self.students[self.get_student_index(info)]['DoB'] )
            elif number == 4:
                print(self.students[self.get_student_index(info)]['Sex'] )
            elif number == 5:
                print(self.students[self.get_student_index(info)]['Address'] )
            elif number == 6:
                print(self.students[self.get_student_index(info)]['Mobile_Number'] )
            elif number == 7:
                print(self.students[self.get_student_index(info)]['Email'] )

            check = input('Do you want to continue (y/n): ')

class Subjects(Student):
    def __init__(self):
        self.subjects = Student._load_json('subjects.json')['subjects']['subject']
        super().__init__()

    def get_subject_index(self, subject_info):
        for index, subject in enumerate(self.subjects):
            if subject['Student_ID'] == subject_info or subject['Name'] == subject_info:
                return index
    
    def _insert_of_edit_json(self):
        student_dict = Student._load_json('subjects.json')
        student_dict['subjects'] = {'subjects': self.subjects}
        return student_dict

    def get_info(self):
        pass

    def insert(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def search(self):
        pass

class Score(Student):
    def __init__(self):
        self.scores = Student._load_json('scores.json')['subjects']['subject']
        super().__init__()

    def get_subject_index(self, score_info):
        for index, score in enumerate(self.scores):
            if score['Student_ID'] == score_info or score['Name'] == score_info:
                return index
    
    def _insert_of_edit_json(self):
        student_dict = Student._load_json('scores.json')
        student_dict['scores'] = {'score': self.scores}
        return student_dict
    
    def get_info(self):
        pass

    def insert(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def search(self):
        pass

    def analysis():
        pass

    def average_score():
        pass

        
    





