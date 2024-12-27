def rotateLeft(d, arr):
    """
    perform 'd' left rotations on the array 'arr'

    parameters:
    d (int): n. or rotations
    arr (list): the array to rotate


    returns:
    list: the rotated array
    """

    #step_1: optimize the n. of rotations
    n = len(arr)
    d = d % n #avoid unnecessary full rotations if d>= n


    #step_2: use the slicing to rearrange the array
    # first_part: arr[d:] (from index 'd' to the end)
    #second_part: arr[:d] (from index '0' to 'd-1')

    rotated_array = arr[d:] + arr[:d]


    #step_3: return the rotated array
    return rotated_array