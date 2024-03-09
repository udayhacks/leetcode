def countDigits(n: int) -> int:  
    count = 0 
    k = n 
    while  n > 0 :

        j = n%10
        if k %j==0:
            count+=1
        n = n //10


    return count



countDigits(35)