# # lcs = longest common subsquence 





# from numpy import matrix


# def lcs(a,b,n,m) :
#     if dp[n][m] != -1 :
#         return dp[n][m]
#     if  n==0 or m ==0 :
#         dp[n][m] = 0
#     else:
#         if a[n-1]  == b[m-1]:
#             dp[n][m] = 1+lcs(a,b,n-1,m-1)
#         else:
#             dp[n][m] = max (lcs(a,b,n-1,m),lcs(a,b,n,m-1))
#     return dp[n][m]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def lcsT(a,b):
    
    m = len(a)
    n = len(b)
    matrix = [[None]*(n+1) for i in range(m+1)]
    ans = []
    
    for i in range(m+1) :
        for j in range(n+1):
            if i == 0 or j == 0  :
                matrix[i][j] = 0        
            elif a[i-1] == b[j-1] :
                    
                    matrix[i][j]= 1+matrix[i-1][j-1]
            else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])   
                    
          
          
              
                    
    while i > 0 and j >0 :
        if a[i-1] == b[j-1] :
            ans.append(a[i-1])
            i-=1
            j-=1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i-=1
        else:
            j-=1
            
    return ans
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
a = "abxyzn"
b = "axgyn"
dp =[[-1]*10 for i in range(11)]
#ans = lcs(a,b,len(a),len(b))
an = lcsT(a,b)
print(an)
