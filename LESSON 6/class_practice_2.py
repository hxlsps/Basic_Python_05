#1 Define a class named Student and initialize attributes: name, age, email and sex. Create a new object of that class.
class Student:
    def __init__(self,name,age,email,sex):
        self.name=name
        self.age=age
        self.email=email
        self.sex=sex

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_sex(self):
        return self.sex

    def set_name(self,name):
        self.name=name
    
    def set_age(self,age):
        self.age=age

    def set_email(self,email):
        self.email=email

    def set_sex(self,sex):
        self.sex=sex

student_1=Student('Loc',22,'xuanloc11042000@gmail.com','male')

#2 Define a class named People with no attributes and mothods. Create a new object of that class.
class People:
    def __init__(self):
        pass

person_1=People()

#3
#3.1  Define a class named Staff with attributes: role, department, salary and a method named show_details() to display all attributes
class Staff:
    def __init__(self,role,department,salary):
        self.role=role
        self._department=department
        self.__salary=salary

    def show_details(self):
        print(f'Role: {self.role}')
        print(f'Department: {self._department}')
        print(f'Salary: {self.__salary}')

    def get_salary(self):
        return self.__salary
    
staff_1=Staff('maid','maid',3000)
staff_1.show_details()

#3.2 Define a class named Student with inherited from Staff class. This class has more 2 attributes: name and age
class Student(Staff):
    def __init__(self, role, department, salary, name, age):
        self.name=name
        self.age=age
        super().__init__(role,department,salary)
    
    def show_details(self):
        print(f'Role: {self.role}')
        print(f'Department: {self._department}')
        print(f'Salary: {self.get_salary()}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

# 3.3 Create a new object of Student then show all attributes of that object.
student_1=Student('dev','dev',2000,'Loc',22)
student_1.show_details()

#4
import math
# 4.1 Define a class named Geometry with 2 methods: get_area() and get_perimeter().
class Geometry:
    def __init__(self):
        pass    
    def get_area(self):
        pass
    
    def get_perimeter(self):
        pass

#  4.2 Define a class named Rectangle which inherited from Geometry class. This class has 2 attributes are length and width. Override two methods from its parrent
class Rectangle(Geometry):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def get_area(self):
        return (self.length+self.width)*2
    
    def get_perimeter(self):
        return self.length*self.width 

# 4.3 Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. Override 2 methods of its parrent  class.
import math
class Circle(Geometry):
    def __init__(self,radius):
        self.radius=radius
    
    def get_area(self):
        return math.pi*self.radius**2
    
    def get_perimeter(self):
        return 2*math.pi*self.radius

# 4.4 Create a new object of class Square and a new object of class Circle. Print area and primeter of those.
rec_1=Rectangle(6,12)
print(f'RECTANGLE 1: Area: {rec_1.get_area()}, Perimeter:{rec_1.get_perimeter()}')
circ_1=Circle(3)
print(f'CIRCLE 1: Area: {circ_1.get_area():.2f}, Perimeter:{circ_1.get_perimeter():.2f}')
