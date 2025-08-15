"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

"""
from collections import Counter
def uniquechar(s):
    count = Counter(s)   # Counter gives o/p as {'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1}

    for i, val in enumerate(s):
        if count[val] == 1:
            return i
        
    return -1

s = "loveleetcode"
print(uniquechar(s))