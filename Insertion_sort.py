# Insertion sorting algorithm

arr = [5,2,9,6,1]

for i in range(0, len(arr)):
    a = arr[i]
    for j in range(i+2):
        if arr[i] > arr[j]:
            arr[i] = arr[j]
        j -= 1
        arr[j+1] = a
    
print(arr)