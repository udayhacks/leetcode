n = 125 




# formula for tailing zero are n/5+n/25...... for n/q  where q <= n .

def tailing_zero(n):
    i = 5
    ans = 0
    while i <= n :
        ans += n//i 
        i *=5
     
     
tailing_zero(251)   
        
        
        
def gcd(a,b):
    if b == 0 :
        return a 
    return gcd(b, a%b) 

gcd(12,36)
