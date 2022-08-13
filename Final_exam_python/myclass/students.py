from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self):
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