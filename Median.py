def Median(num1, num2):
    arr = num1 + num2
    print(arr)
    lst1 = []
    lst2 = []
    total = sum(arr)//len(arr)

    print(total)
    for i in range(0, len(arr)):
        if arr[i] == total:
            pass
num1 = [2,2,4,4]   
num2 = [2,2,2,4,4]

res = Median(num1, num2)
print(res)