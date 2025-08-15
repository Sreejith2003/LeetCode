def rotate(arr, d):
    """
    1) First solution normal position changing
    
        lst = []
        
        for i in range(d, len(arr)):
            lst.append(arr[i])
        #print(lst)

        for j in range(0, d):
            lst.append(arr[j])

        #print(lst)
        return lst

    2) Second solution not a best solution for roating a array

        lst = arr[d::]
        lst.append(arr[:d])
        #print(lst)

        for i in range(0, len(lst)):
            if isinstance(lst[i], list):
                lst[i:i+1] = lst[i]
        return lst
    """

# Best solution works for all test cases 
    n = len(arr)
    d %= n

    arr[:] = arr[d::] + arr[:d]

    return arr


arr = [1, 2, 3, 4, 5]
d = 2
res = rotate(arr, d)
print(res)