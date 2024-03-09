def nBinaryTriangle(n: int) -> None:
    for i in range(1,n+1):
        if i %2 == 0 :
            start = 0
        else:
            start = 1
        for j in range(i):
            print(start,end = "")
            start = 1-start 
        print()





def nBinaryTriangle(n: int) -> None:

    # Initialise 'num'.
    num = 1
    for i in range(n):
        for j in range(1, num+1):
            print((i + j) & 1, end=" ")

        # End the current line.
        print()

        num += 1
nBinaryTriangle(3)
