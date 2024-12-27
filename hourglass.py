def hourglass(arr):
    # initnialize a max low n to be starting point
    max_sum = -float('inf') # this ensures that even the negative n.s are considered



    # loop through each possible hourglass center
    # we need 3x3 grid to fit without going out boubds
    for i in range(4):
        for j in range(4):
            # caculate the sum of the hourglass with the center at arr[i+1][j+1]
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]


            # sum of the current hourglass 
            hourglass_sum = top + mid+ bot

            # upadte the max_sum if we find a larger hourglass sum
            max_sum = max(max_sum, hourglass_sum)

    return max_sum

