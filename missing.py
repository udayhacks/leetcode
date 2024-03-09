def missingNumber(a, N ) -> int:
    n = N
    l= []
    for i in range(1,(n//2)+1):
        l.append(i)
        l.append(n-i)
        if i not in a :
            return i 

        if n-i not in a :
            return n-i 

    return n 




missingNumber([1,2,3,4,5,6,7,8],8)