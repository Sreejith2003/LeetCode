# Selection sorting algorithm

"""
This sorting technique repeatedly finds the minimum element and sort it in order. 
Bubble Sort does not occupy any extra memory space. 
During the execution of this algorithm, two subarrays are maintained, the subarray which is already sorted, 
and the remaining subarray which is unsorted. During the execution of Selection Sort for every iteration, 
the minimum element of the unsorted subarray is arranged in the sorted subarray. Selection Sort is a more efficient algorithm than bubble sort. 
Sort has a Time-Complexity of O(n2) in the average, worst, and in the best cases.

"""

arr = [5,2,9,6,1]
n = len(arr)
i = 0

while i != n:
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    
print(arr)

# Time complexity is O(n2)