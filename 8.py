class Solution:
    def myAtoi(self, s: str) -> int:

        ans = 0 
        sign = 1 

        s = s.lstrip()
        if not s :
            return ans

        if s[0] == "-" :
            sign = -1
        
        for i in range(1,len(s)):
            if not s[i].isdigit():
                break
            else:
                ans = (ans *10) + int(s[i])


        if ans > 2**31-1:
            return 2**31-1
        elif ans <= -2**31 :
            return -2**31
        else:
            return ans*sign


                
                
        
    
    
a = Solution()
l = a.myAtoi("1337c0d3")
k= a.myAtoi("words and 987")
j = a.myAtoi(" -042")
ans = [l,k,j]
for i in ans :
    print(i)       

            

