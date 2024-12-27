def matchingStrings(stringList, queries):
    # create an empty list to store teh results 
    results = []


    # loop through each query string in the list 'queries'
    for query in queries:
        # count the occurrences of the current query in 'stringList'
        count = stringList.count(query)
        results.append(count)


    return results