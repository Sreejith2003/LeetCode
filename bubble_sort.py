# Bubble Sorting

"""
Bubble Sort is a simple sorting algorithm. 
This sorting algorithm repeatedly compares two adjacent elements and swaps them if they are in the wrong order. 
It is also known as the sinking sort. 
It has a time complexity of O(n2) in the average and worst cases scenarios and O(n) in the best-case scenario. 
Bubble sort can be visualized as a queue where people arrange themselves by swapping with each other so that 
they all can stand in ascending order of their heights. 
Or in other words, we compare two adjacent elements and see if their order is wrong, if the order is wrong we swap them. 
(i.e arr[i] > arr[j] for 1 <= i < j <= s; where s is the size of the array, if array is to be in ascending order, and vice-versa).

"""
     

arr = [5,2,9,6,1]
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


# Both are O(n2) Time complexity
