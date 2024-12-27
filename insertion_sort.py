def insertion_sort():
    # loop through the array starting from the second element
    for i in range(1, len(l)):
        key = l[i] # current element to insert
        j = i - 1 # index of the previous element



        #while the current element is smaller than its predecessor 
        # and we haven't reached the start of the array

        while j >= 0 and l[j] > key:
            l[j + 1] = l[j] #shift the larger element to the right


            j -= 1 #move to the previous element


        l[j + 1] = key #insert the 'key at the correct position



#input the size of the array
m = int(input().strip())



#input the array elements as integers
ar = [int(i) for i in input().strip().split()]


#call the sorting function
insertion_sort(ar)


#print the sorted array, space-separated, as a single line
print(" ".join(map(str, ar)))




