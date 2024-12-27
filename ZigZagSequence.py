def findZigZagSequence(a, n):
    #step_1: sort the array to make it lexicographically smallest
    a.sort() # ensure that we start with the smallest permutation

    # step_2: find the middle index
    mid = (n -1) // 2


    # step_3: swap the middle element with the last one
    a[mid], a[n-1] = a[n-1], a[mid]

    # step_4: reverse the second half of the array
    st = mid + 1 # start of the second half
    ed = n - 2 # end of the second half

    while st <= ed:
        a[st], a[ed] =a[ed], a[st] #swap elmenets to reverse the second half
        st += 1
        ed -= 1


    #step_5: print the result as a single line of space-separated integers
    print(' '.join(map(str, a))) # converts list elements to strings and joins with spaces
    
     
