from math import pi


def numberCrown(n: int) -> None:

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for h in range(2*n-2*i):
            print(" ",end="")
        for k in range(i,0,-1):
            print(k,end=" ")
        print()





'''
    Time Complexity - O( N * N )
    Space Complexity - O( 1 )

    where N is the given input.
'''
"""

def numberCrown(n: int) -> None:

    # Initialise 'num'.
    num = 1
    gap = (n - 1) * 2
    for i in range(n):
        currentNumber = 1
        for j in range(1, num+1):
            print(currentNumber, end=" ")
            currentNumber += 1
        for j in range(1, gap+1):
            print("#", end=" ")
        currentNumber -= 1
        for j in range(1, num+1):
            print(currentNumber, end=" ")
            currentNumber -= 1
        
        # End the current line.
        print()

        num += 1
        gap -= 2
"""

numberCrown(3)