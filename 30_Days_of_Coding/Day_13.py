# Abstract Classes

from abc import ABCMeta, abstractmethod

class Book(metaclass=ABCMeta):
    #declared as Abstract Base Class by specifying the metaclass 'ABCMeta'
    def __init__(self, title, author):
        # constructor initialises the 'title' and 'author' attributes
        self.title = title 
        self.author = author



        @abstractmethod
        # decorator marks this method as abstract
        def display(self):
            pass

class MyBook(Book):
    # subclass of 'Book', inhert all its attributes and methods
    def __init__(self, title, author, price):
        # constructor inializes 'title', 'author' and 'price'
        super().__init__(title, author) # super(), calls the constructor of the parent class 'Book'
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


if __name__ == "__main__":

    title, author, price = input(), input(), int(input())


    new_novel = MyBook(title, author, price)


    new_novel.display()

