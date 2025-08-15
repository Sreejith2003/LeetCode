def removeChars(string1, string2):
    lst = []
    # count = 0
    # j = count
    lst1 = list(string1)
    lst2 = list(string2)
    n = len(lst1)
    for i in range(0, len(lst2)): 
        for j in range(0, n):     
            if j > n:
                i += 1 
                count = 0
                j = count
                
            if lst2[i] in lst1[j]:
                lst1.remove(lst1[j])
                #lst.append(lst1[j])
                #print(lst1)

                n = len(lst1) -1
    #             count = 0
    #             j = count
                  
    return "".join(lst1)



    
    # for val in lst1:
    #     print(type(lst1))
    #     if lst2[val] in lst1:
    #         lst1.remove(val)


    #     return "".join(lst1)
        
string1 = "occurrence"
string2 = "car"

res = removeChars(string1, string2)
print(res)