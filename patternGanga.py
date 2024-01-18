def pattern(n):
    
    k=0
    j = n-1
    for i in range(n,-1,-1):
        l = i*(10**j)
        k+=l
        j-=1
    
    k = int(k)


    for j in range(1,n+1):
        if j == 1 :
            l =k//(10**j)
            print(l,end="")
            print(*["*"])
            j+=1
        elif j ==n:
            print(*["*"],end="")
            print(k%(10**(j-1)))
            
            
        else:
            l =k//(10**j)
            print(l,end="")
            print(*["*"],end="")
            print(k%(10**(j-1)))


pattern(8)