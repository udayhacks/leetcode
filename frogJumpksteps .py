import sys

def minimizeCost(n : int, k : int, heights):
    dp= [-1]*n
    dp[0]= 0

    for i in range(1,n):
        mn =  sys.maxsize

        for j in range(1,k+1):
            jj = i -j 
            if jj >= 0 :
                jump = dp[jj]+abs(heights[i]-heights[jj])
                mn = min(jump,mn)
        dp[i] = mn

    return dp[n-1]


l = [10 ,40 ,50 ,20 ,60]
l= [10, 40, 30, 10]
k = 2

minimizeCost(len(l),k,l)