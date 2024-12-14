

class Solution:
    def betterString(self, str1, str2):
        
        
        
        
        def subs(n,ans,i,dp,a):
            if i == n:
                k = "".join(ans[:i])
                if k not in dp :
                    dp[k] = 1
                else:
                    dp[k] +=1
                return 
            ans.append(a[i])
            subs(n,ans,i+1,dp,a)
            ans.pop()
            subs(n,ans,i+1,dp,a)
            
            
            
        dp1= {}
        dp2 ={}
        n = len(str1)
        
        s1 = list(str1)
        s2 = list(str2)
        
        
        subs(n,[],0,dp1,s1)
        subs(n,[],0,dp2,s2)
        
        c = 0 
        l = 0
        
        for i , j in dp1.items():
            if j ==1 :
                c+=1
        for i , j in dp2.items():
            if j ==1 :
                l+=1
                
        if c >= l  :
            return str1
        if c <l :
            return str2
            
                
        
           
        
        
  
a= Solution()
k = a.betterString("gfg","ggg")    
print(k)