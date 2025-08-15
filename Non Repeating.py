from collections import Counter
def NonRepeating(s):
# Time Complexity O(n2)

    # lst = list(s)
    # n = len(lst)
    # #i = 0
    # for i in range(0, n):   
    #     count = lst.count(lst[i])
    #     if count == 1:
    #         return lst[i]
        
    # return -1

# Method 2 --> Time Complexity is O(n)

    count = Counter(s)  # This gives {'e': 4, 'g': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}
    
    for char in s:
        if count[char] == 1:
            
            return char
        
    return "$"
                        
s = "geeksforgeeks"
res = NonRepeating(s)
print(res)