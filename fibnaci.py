
def fib(n):
    prev2= 1
    prev1= 1 
    for i in range(2,n):
        prev = prev2+prev1 
        prev2 = prev1
        prev1 = prev
         


    return prev1 


print(fib(5))