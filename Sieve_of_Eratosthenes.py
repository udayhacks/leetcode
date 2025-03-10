

""" 


 """



def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will  
    
    prime = [1 for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == 1):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = 0
        p += 1

    # Print all prime numbers
   
   
    return prime
            
left =1
right = 1000000000000
l= SieveOfEratosthenes(right)
k = []
for i in range(left,right+1):
    if  i >1 and l[i] == 1:
        k.append(i)
    
    
print(k)
mn =100000
a = -1
b = -1
for i in range(len(k)-1,0,-1):
    
    if k[i] - k[i-1] <= mn:
        mn = min(k[i] - k[i-1],mn)
        a = k[i]
        b = k[i-1]
print(b,a)
        
    