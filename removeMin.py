def removeMin(arr):
    Max = max(arr)
    Min = min(arr)
    count = 0
    arr.sort()
    n = len(arr)
    # while((2*Min) <= Max):
    #     # arr.remove(Max)
    #     # Max = max(arr)
    #     # count += 1

    #     arr.remove(Min)
    #     Min = min(arr)
    #     count += 1
    # return count

    for i in range(0, n):
        if((2*Min) >= Max):
            return count
        
        else:
            if Max >= 100:
                arr.remove(Max)
                n = len(arr)
                count += 1
                Max = max(arr)

            else:
                arr.remove(Min)
                Min = min(arr)
                n = len(arr)
                count += 1
    return count 


arr = [1,25,35,42,68,70] # [1,25,35,42,68,70]
print(removeMin(arr))