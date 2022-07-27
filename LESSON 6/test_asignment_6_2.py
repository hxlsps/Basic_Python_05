class Mother:
    def __init__(self):
        pass

    def display_message(self):
        print('ABC')

class Daughter(Mother):
    def __init__(self):
        pass

    def display_message(self):
        print('DEF')

def main():
    daugther_1 = Daughter()
    daugther_1.display_message()

main()