"""
1) Output:

        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9

"""

def pyramid(n):
    for i in range(0, n+1):
        
        for j in range(n-i):
            print(" ", end = " ")

        for j in range(2 * i - 1):
            print(j+1, end = " ")

        print()

pyramid(5)
print()

"""
2) Output:

        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5

"""

def numericalpyramid(n):
    for i in range(1, n+1):
        
        for j in range(1, n-i+1):
          print(" ",end = " ")
        for j in range(i, 0, -1):
            print(j, end=" ")

        for j in range(2, i+1):
            print(j, end = " ")
        
        print()

numericalpyramid(5)
print()


"""
3) Output:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""

def Reverserighttriangle(n):
    for i in range(0, n+1):
      
      for j in range(1, n-i+1):
          print(j, end = " ")
      print()
Reverserighttriangle(5)
print()



"""
4) Output:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

def RightTriangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = " ")

        print()

RightTriangle(5)
print()


"""
5) Output:

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

"""

def rightTriangle(n):
  for i in range(0, n):
      for j in range(i, -1, -1):
          print(j+1, end=" ")
      
      print()
rightTriangle(5)
print()

"""
6) Output:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

def rightTriangle1(n):
  for i in range(0, n):
      for j in range(i, -1, -1):
          print(i+1, end=" ")
      
      print()
rightTriangle1(5)


"""
7) Output:

"""

def triangle1(n):
    for i in range(0, n+1):
        
        for j in range(1, i*2):
            print(" ", end=" ")
        for j in range(2*i-1):
          print(j+1, end = " ")
        print()
triangle1(5)