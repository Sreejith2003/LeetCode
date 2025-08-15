def largestvalue(arr):

    """
    lst = []

    arr = list(set(arr))
    #print(arr)
    if len(arr) == 1 or len(arr) == 0:
        return -1
    
    Max = max(arr)
    arr.sort()
    

    for i in range(0, len(arr)):
        
        if Max > arr[i]:
            lst.append(arr[i])
    
    return max(lst)
    """

    arr = list(set(arr))  
    
    if len(arr) < 2:  
        return -1

    first, second = float('-inf'), float('-inf')

    for num in arr:
        if num > first:
            second, first = first, num  # second will be updated as first and first will be as num
        elif num > second:
            second = num  

    return second

arr = [12, 35, 1, 10, 34, 1]
print(largestvalue(arr))
