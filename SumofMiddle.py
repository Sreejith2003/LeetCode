def sumOfMiddle(arr1, arr2):

    arr = arr1+arr2
    arr.sort()
    mid = len(arr) // 2

    print(mid)
    print(arr)
    # i = 0
    # while arr[i] < mid:
    #     i += 1

    # return mid + arr[i+1]
    i = 0
    for j in range(len(arr), 0):
        if i == mid:
            return arr[i]+ arr[j]
        else:
            i += 1

    

arr1 = [1, 12, 15, 26, 38] 
arr2 = [2, 13, 17, 30, 45]

print(sumOfMiddle(arr1, arr2))