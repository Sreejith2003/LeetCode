"""
1) Output:

    *
   ***
  *****
 *******
*********

"""


def starpattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end = "")

        for k in range(1, 2*i):
            print("*", end = "")

        print()

starpattern(5)

print()

"""
2) Output:

*********
 *******
  *****
   ***
    *

"""

def reverseStarPattern(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end = "")
            
        for k in range(2*i-1):
            print("*", end = "")
        
        print()

reverseStarPattern(5)
print()

"""
3) Output:

    *
   * *
  *   *
 *     *
*********

"""
def HollowPyramid(n):
    for i in range(1, n+1):
        for j in range(1, 2*n):
            if j == n - i + 1 or j == n + i - 1 or i == n:
                print("*", end = "")
            else:
                print(" ", end = "")

        print()

HollowPyramid(5)
print()

"""
4) Output:

* * * * *
*       *
*       *
*       *
* * * * *

"""

def SquareHollowPattern(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 or i == n or j == 1 or j == m:
                print("*", end = " ")
            else:
                print(" ", end=" ")

        print()
        
SquareHollowPattern(5,5)