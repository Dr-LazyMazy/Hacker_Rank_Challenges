# Abstract Classes

from abc import ABCMeta, abstractmethod

class Book(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass

# Write MyBook class
class MyBook(Book):
    # constructor to initialize title, author, and price
    def __init__(self, title, author, price):
        self.title, self.author, self.price = title, author, price

        # implement the abstract method 'display'
        def display(self):
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Price: {self.price}")


# read the input
if __name__ == "__main__":
    title, author, price = input(), input(), int(input())

    # create an instance of MyBook
    new_novel = MyBook(title, author, price)

    # call the display method
    new_novel.display()