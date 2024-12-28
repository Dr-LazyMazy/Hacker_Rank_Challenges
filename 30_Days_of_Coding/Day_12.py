# Day_12: Inheritance

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self. lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # constructor for stduent class
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber) # initialize the aprent class properties
        self.scores = scores



    # method to calculate grade
    def calculate(self):
        average = sum(self.scores) / len(self.scores)


        # Determine the grade based on avaerage
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average <= 90:
            return 'E'
        elif 70 <= average <= 80:
            return 'A'
        elif 55 <= average <= 70:
            return 'P'
        elif 40 <= average <= 55:
            return 'D'
        else:
            return 'T'
        

# Input Reading and Output
if __name__ == "__main__":
    # Read the input
    firstName, lastName, idNumber = input().split()
    idNumber = int(idNumber)
    numScores = int(input())
    scores = list(map(int, input().split()))


    # create a Stduent Object
    stduent = Student(firstName, lastName, idNumber, socres)


    # Output results
    stduent.printPerson()
    print("Grade:", stduent.calculate())

