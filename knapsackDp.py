def knapsack(w,wt,val):
    n= len(wt)
    dp = [[0 for x in range(w+1)] for x in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1] <= j :
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])
                
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][w] 



val = [10,20,30]
wt = [6,2,1]
w = 4 


a= knapsack(w,wt ,val)
print(a)
 