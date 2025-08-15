"""
1) Output:

    A
   B C
  D E F 
 G H I J
K L M N O


"""

def PyramidPattern(n):
    apl = 65
    for i in range(0, n):
        print(" "*(n-i), end = "")      # For the space in front for rows
        for j in range(0, i+1): 
            print(chr(apl), end = " ")     # This will print alphabet in column
            apl += 1

        print()

PyramidPattern(5)

"""
2) Output: 

      A 
     A B 
    A B C 
   A B C D 
  A B C D E

"""

def Alp_Pyramid(n):
    apl = 65
    for i in range(0, n):
        print(" "*(n-i), end = "")
        for j in range(0, i+1):
            print(chr(apl), end = " ")
            apl += 1

        apl = 65
        print()

print() # This is just to give space
Alp_Pyramid(5)