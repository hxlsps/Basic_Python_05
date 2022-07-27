class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def set_name(self,name):
        self.name = name
    
    def set_age(self,age):
        self.age = age

class Zebra(Animal):
    def __init__(self,name,age,origin):
        super().__init__(name,age)
        self.origin=origin
    
    def message(self):
        print(f'Name: {self.name}, Age: {self.age}, Origin: {self.origin}')

class Dolphin(Animal):
    def __init__(self,name,age,origin):
        super().__init__(name,age)
        self.origin=origin
    
    def message(self):
        print(f'Name: {self.name}, Age: {self.age}, Origin: {self.origin}')

def main():
    zeb_1=Zebra('Zebra',19,'Africa')
    zeb_1.message()
    dol_1=Dolphin('Dolphin',22,'ocean')
    dol_1.message()

main()
