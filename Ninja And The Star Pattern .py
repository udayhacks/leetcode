def getStarPattern(n: int) -> None:
    for i in range(n):
        if i==0 or i == n-1 :
            print("*"*n)

        else:
            for i in range(n):
                if i ==0 or i == n-1:
                    print("*",end="")
                else:
                    print(" ",end = "")

            print()



        
