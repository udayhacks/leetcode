
    

def countDistinctWays(nStairs: int,dp={}) -> int:
    if nStairs in dp :
        return dp[nStairs]
    
    if nStairs== 0 or nStairs==1 :
        return 1 
    if nStairs < 0 :
        return 0 
    one=countDistinctWays(nStairs-1,dp) 
    two=countDistinctWays(nStairs-2,dp)
    
    return one+two
    
    



def countDistinctWays(n):
    


    
a= countDistinctWays(7)
print(a)
print((a//76)//(662189184 ))