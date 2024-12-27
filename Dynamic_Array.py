# dynamic_Array challenge
def dynamicArray(n, queries):
    # setp_1: initialize 'n' empty lists inside a main list called 'arr'
    arr = [[] for _ in range(n)] # creates a list of 'n' empty sub-lists
    lastAnswer = 0 # initialize lastAnswer to 0 as per problem requirment
    results = [] #store the output for each query


    #step_2: process each query one by one
    for query in queries:
        # unpack the query into three parts: type_of_query, x, and y
        type_of_query, x, y = query


        # calculate idx using the formula given in the problem
        idx = (x ^ lastAnswer) % n 


        #if it's a query type 1: append 'y' to arr[idx]
        if type_of_query == 1:
            arr[idx].append(y)


        #if it's a query type 2: retrieve value from 'arr[idx]' and update lastAnswer
        elif type_of_query == 2:
            # fid the element at position 'y % len(arr[idx])' in 'arr[idx]'
            value = arr[idx][y % len(arr[idx])]
            lastAnswer = value # update lastAnswer with this value



            # add the new lastAnswer to the results list
            results.append(lastAnswer)


    return results