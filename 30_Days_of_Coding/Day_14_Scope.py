# Day_14 Scope

# Find the difference between two elements, 'max absolute'

class Difference:
    # initialize a constructor for the class
    def __init__(self, elements):
        # create the private instance, it store the list of ints
        self.__elements = elements
        # create a public instance and initialisez to None
        self.maximumDifference = None


    # create a method to compute the difference between the max and min number
    def computeDifference(self):
        max_element = max(self.__elements)
        min_element = min(self.__elements)



        # find the absoljute difference between largest and smallest numbers, and store it to the parameter "maximumDifference"
        self.maximumDifference = abs(max_element - min_element)




if __name__ == "__main__":
    # read the input
    _ = input() # read the size of the array
    a = [int(e) for e in input().split(' ')] # reda the array elements


    d = Difference(a) #create the 'Difference' Object

    d.computeDifference() # compute the max difference


    print(d.maximumDifference) # print the max difference
