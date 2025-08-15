# Find the sum of a nested list → [1,2,3,[2,3,4,[5,6]]]

"""
The isinstance() function in Python is a built-in function used to determine 
if an object is an instance of a specified class or any of its subclasses. 

example:
x = 10
y = "hello"
z = [1, 2, 3]

print(isinstance(x, int))         # Output: True
print(isinstance(y, str))         # Output: True
print(isinstance(z, list))        # Output: True

"""

def sum_nested_list(nested_list):

    total = 0
    for ele in nested_list:
        if isinstance(ele, list):  # isintance() checks if ele is list or not

            total += sum_nested_list(ele)

        else:
            total += ele
        
    return total

nested_list =  [1,2,3,[2,3,4,[5,6]]]
print(sum_nested_list(nested_list))