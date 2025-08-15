#import collections 

def findValidPair(s):
    
    hash_map = {}
    for ele in s:
        if ele not in hash_map:
            hash_map[ele] = 1
        else:
            hash_map[ele] += 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            chr_int1 = int(s[i])
            chr_int2 = int(s[i-1]) 

            if hash_map[s[i]] == chr_int1 and chr_int2 == hash_map[s[i-1]]:
                return s[i-1: i+1]
    return ""




s = "21333"

print(findValidPair(s))