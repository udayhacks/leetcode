class Solution:
    def func1(self,s,n,k,ans):
        
        if k == n :
            k ="".join(s[:n])
            ans.append(k)
            return  
        if s[n-1] =="1" :
            s[n] = "0"
            self.func1(s,n+1,k,ans)
        if s[n-1] == "0":
            s[n] = "0"
            self.func1(s,n+1,k,ans)
            s[n] ="1"
            self.func1(s,n+1,k,ans)
            
    def func(self,k):
        if k <=0:
            return 
        ans = []
        s =[0]*k
        s[0]="0"
        self.func1(s,1,k,ans) 
        s[0] ="1"
        self.func1(s,1,k,ans) 
        
        return ans
        
        
        



a = Solution()
print(str(a.func(3)))



l = "12"
print(type(l[0]),id(l))
l= list(l)
print(l)
print(type(l),id(l))