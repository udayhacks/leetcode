class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        p = []
        for i in range(len(s)) :
            if s[i] == "1":
                p.append(i)
        d = []
        
        
        for i in p :
            c= 0 
            l = ""
            for j in range(i, len(s)) :
                if s[j] == "1":
                    c+=1 
                l+=s[j]
                if c == k  :
                    d.append(l)
                    break
                
        ans = d[0]
        n = len(ans)
                
        for i in d:
            if len(i) < n :
                ans = i
                n = len(ans)
                
        return ans
            
                
                
                
                    
  
"""       
#Submission Result: Wrong Answer 
#Input:

k =10
#Output:
"11101011011011"
#Expected:
"10101101101111"                """
                    
                    
a = Solution()

"""s = "1011"
k = 2
"""

s ="001110101101101111"
k= 10 

















"""






"1100100101011001001"
7
Output:
"100101011001001"
Expected:
"1100100101011"



"""

s= "1100100101011001001"
k =7


s = "100011001" 
k = 3

a.shortestBeautifulSubstring(s,k)
                    
                    