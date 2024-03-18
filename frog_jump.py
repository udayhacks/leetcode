

import sys
def frog(n,arr,dp):
    if n == 0 :
        return 0 
    if dp[n] !=-1 :
        return dp[n]
    two = sys.maxsize
    one = frog(n-1,arr,dp)+(abs(arr[n]-arr[n-1]))
    if n >1 :
        two = frog(n-2,arr,dp)+(abs(arr[n]-arr[n-2])) 
        
    dp[n] = min(one , two ) 
    return dp[n] 

if __name__ == "__main__" :
    n = 6
    dp=[-1]*n
    height = [30, 10, 60, 10, 60, 50]
    a=frog(n-1,height,dp)
    print(a)