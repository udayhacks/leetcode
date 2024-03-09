def getNumberPattern(n: int) -> None:
    for i in range(2*n-1):
        if i == 0 or i == 2*n-1 :
            for i in range(2*n-1):
                print(n,end="")

        else:
            start = n
            for j  in range(n):
              
                if i >= j:
                    print(start,end="")
                    start-=1
                else:
                    break
            hh= ((2*n-1)-2*i)-1
            for k in range(hh-1) :
                print(start+1,end="")

            for l in range(i+1):
                start+=1
                print(start,end="")
               

            
        print()

getNumberPattern(5)